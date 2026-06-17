# Contributing to ZeroEye

Thank you for your interest in contributing to the ZeroEye project! We welcome contributions of all kinds, from bug fixes and feature requests to documentation improvements.

## 🚀 Getting Started

### Prerequisites

Depending on which part of the project you are working on, you will need the following tools installed:

- **Backend**: Rust (Cargo)
- **Frontend**: Node.js (npm)
- **Market Infrastructure**: Go
- **Sandbox (Frailbox)**: C/C++ (GCC, CMake, Make)
- **Compliance**: Java (JDK)
- **Scripts/Tools**: Python 3, Ruby, Lua, Haskell (GHC)

### Local Build Instructions

The project uses a unified build system implemented in Python. To build all modules:

```bash
python3 build.py
```

To build a specific module:
```bash
python3 build.py -m <module_name>
```

Available modules include: `backend`, `frontend`, `market`, `frailbox`, `engine`, `compliance`, `v2-market-stream`, `nfc-scanner`, `openapi-haskell`, and `openapi-tools`.

For a detailed build log, use the `--verbose` flag:
```bash
python3 build.py --verbose
```

---

## 🛠 Development Workflow

### 1. Find an Issue
We encourage contributors to look for issues tagged as `help wanted` or `good first issue`. Many of our tasks have associated **bounties** — check the issue descriptions for details.

### 2. Create a Branch
Always create a new branch for your changes:
```bash
git checkout -b feat/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

### 3. Implementation & Testing
- Ensure your code follows the project's style guidelines.
- For C/C++ modules, compile with `-Wall -Wextra -Werror` to catch potential issues.
- For Rust, ensure `cargo fmt` and `cargo clippy` pass.
- Verify your changes by running the corresponding module build via `build.py`.

### 4. Submit a Pull Request
- Push your branch to your fork.
- Open a PR against the `main` branch.
- Provide a clear description of your changes.
- If the PR is for a bounty, mention the issue number (e.g., `Fixes #12`).

---

## 📋 PR Guidelines

- **Atomic Commits**: Keep your commits focused on a single change.
- **Descriptive Titles**: Use clear and concise titles for your PRs.
- **Testing Proof**: Include logs or screenshots showing that your changes work as expected.
- **Documentation**: If you add a new feature or change an API, update the corresponding documentation in the `docs/` directory.

## ⚖️ License
This project is licensed under the terms specified in the repository's LICENSE file. By contributing, you agree to abide by these terms.
