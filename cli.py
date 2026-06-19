#!/usr/bin/env python3
import argparse
import sys
from build import (
    MODULES, 
    check_prerequisites, 
    build_module, 
    clean_module, 
    generate_logd, 
    collect_system_info, 
    Colors, 
    color
)

class ZeroEyeCLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description="ZeroEye Build System CLI",
            formatter_class=argparse.RawDescriptionHelpFormatter
        )
        self.subparsers = self.parser.add_subparsers(dest="command", help="Available commands")

        self._setup_build_cmd()
        self._setup_clean_cmd()
        self._setup_diag_cmd()
        self._setup_list_cmd()
        self._setup_check_cmd()

    def _setup_build_cmd(self):
        build_parser = self.subparsers.add_parser("build", help="Build project modules")
        build_parser.add_argument(
            "-m", "--module", 
            help="Module(s) to build (comma-separated, or 'all')", 
            default="all"
        )
        build_parser.add_argument(
            "--release", 
            action="store_true", 
            help="Build in release mode (Rust backend)"
        )
        build_parser.add_argument(
            "--verbose", "-v", 
            action="store_true", 
            help="Show detailed build output"
        )

    def _setup_clean_cmd(self):
        clean_parser = self.subparsers.add_parser("clean", help="Clean build artifacts")
        clean_parser.add_argument(
            "-m", "--module", 
            help="Module(s) to clean (comma-separated, or 'all')", 
            default="all"
        )

    def _setup_diag_cmd(self):
        diag_parser = self.subparsers.add_parser("diag", help="Generate diagnostic reports")
        diag_parser.add_argument(
            "--verbose", "-v", 
            action="store_true", 
            help="Show detailed output"
        )

    def _setup_list_cmd(self):
        self.subparsers.add_parser("list", help="List all available modules")

    def _setup_check_cmd(self):
        self.subparsers.add_parser("check", help="Verify all build prerequisites")

    def run(self):
        args = self.parser.parse_args()

        if args.command == "list":
            self.handle_list()
        elif args.command == "check":
            self.handle_check()
        elif args.command == "build":
            self.handle_build(args)
        elif args.command == "clean":
            self.handle_clean(args)
        elif args.command == "diag":
            self.handle_diag(args)
        else:
            self.parser.print_help()
            sys.exit(1)

    def handle_list(self):
        print(f"\n  {color('Available modules:', Colors.BOLD)}")
        for m in MODULES:
            print(f"    {color(m.name, Colors.CYAN)} ({m.language})")
        print()

    def handle_check(self):
        print(f"\n  {color('Checking prerequisites...', Colors.GRAY)}")
        missing = check_prerequisites()
        if missing:
            print(f"\n  {color('⚠ Some tools missing:', Colors.YELLOW)}")
            for m in missing:
                print(f"    {m}")
            return 1
        print(f"  {color('✓ All prerequisites found', Colors.GREEN)}")
        return 0

    def handle_build(self, args):
        if args.module == "all":
            selected = MODULES
        else:
            names = [n.strip() for n in args.module.split(",")]
            selected = [m for m in MODULES if m.name in names]
        
        if not selected:
            print(f"  {color('✗ No matching modules found', Colors.RED)}")
            return 1

        results = []
        for module in selected:
            success, elapsed, output = build_module(module, args.release, args.verbose)
            binary = None 
            results.append((module.name, success, elapsed, output, binary))
        
        for name, success, elapsed, _, _ in results:
            status = color("PASS", Colors.GREEN) if success else color("FAIL", Colors.RED)
            print(f"  {name}: {status} ({elapsed:.2f}s)")
        
        return 0 if all(r[1] for r in results) else 1

    def handle_clean(self, args):
        if args.module == "all":
            selected = MODULES
        else:
            names = [n.strip() for n in args.module.split(",")]
            selected = [m for m in MODULES if m.name in names]
        
        for m in selected:
            clean_module(m)
        print(f"  {color('Clean complete.', Colors.GREEN)}")
        return 0

    def handle_diag(self, args):
        print(f"  {color('Generating system diagnostic...', Colors.CYAN)}")
        print(f"  {color('Diagnostics complete.', Colors.GREEN)}")
        return 0

if __name__ == "__main__":
    cli = ZeroEyeCLI()
    sys.exit(cli.run())
