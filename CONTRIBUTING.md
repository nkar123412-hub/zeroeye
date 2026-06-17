# Contributing to ZeroEye

Welcome to ZeroEye! We appreciate your interest in contributing to our multi-language ecosystem. ZeroEye is a complex polyglot project combining Rust, Go, TypeScript, C/C++, Java, Ruby, Lua, and Haskell.

## 🛠 Prerequisites

Due to the polyglot nature of the project, you will need several toolchains installed on your system. We recommend using a Linux environment (Ubuntu/Debian).

### Required Toolchains
- **Rust**: `cargo` (for the backend)
- **Node.js & npm**: (for the frontend)
- **Go**: `go` (for the market services)
- **C/C++**: `gcc`, `g++`, `make`, and `cmake` (for Frailbox and the Engine)
- **Java**: `javac` (JDK) (for compliance modules)
- **Ruby**: `ruby` (for v2 services)
- **Lua**: `luac` (for NFC scanner and tools)
- **Haskell**: `ghc` (for OpenAPI generation)
- **Python 3**: (for build orchestration and tools)

---

## 🚀 Build Instructions

### 1. Automatic Build (Recommended)
The easiest way to build all modules is to use the provided orchestration script:

```bash
python3 build.py
```

This script detects your platform, checks for prerequisites, and builds every module in the correct order.

### 2. Manual Module Build
If you are working on a specific part of the project, you can build it individually:

#### Backend (Rust)
```bash
cd backend
cargo build
```

#### Frontend (TypeScript/React)
```bash
cd frontend
npm install
npm run build
```

#### Market (Go)
```bash
cd market
go build -o market .
```

#### Frailbox (C/C++)
```bash
cd frailbox
make
# For the engine:
cd engine
mkdir build && cd build
cmake ..
cmake --build .
```

#### Compliance (Java)
```bash
cd compliance
javac -d build ComplianceAuditor.java
```

---

## 🤝 Development Workflow

### 1. Creating a Branch
Please create a descriptive branch for your changes:
- `feat/feature-name` for new features.
- `fix/bug-description` for bug fixes.
- `docs/update-info` for documentation.

### 2. Pull Request Guidelines
- **Atomic Commits**: Keep commits focused on one logical change.
- **Clear Descriptions**: Explain *why* the change is necessary, not just *what* was changed.
- **Testing**: Ensure your changes don't break existing modules. If you add a new feature, please include a corresponding test or a reproduction script.
- **CI/CD**: Wait for the build scripts to pass before requesting a review.

### 3. Issue Reporting
Before starting a new task, please:
1. Check if a similar issue already exists.
2. Open an issue to discuss your proposed approach.
3. Claim the issue by commenting `/claim`.

## 📜 Project Structure
- `/backend`: Core logic in Rust.
- `/frontend`: React-based UI.
- `/market`: High-performance trading services in Go.
- `/frailbox`: Low-level simulation engine in C/C++.
- `/tools`: Python scripts for migration and diagnostics.
- `/docs`: Technical specifications and OpenAPI schemas.
