# Contributing

All contribution are welcome!!!. When contributing to this repository, please first  check if your contribution is not planned yet, or search in old issues if something similar already exist.

Below you have a few considerations to keep in mind and some examples to help you to use a minimal good practices.

we are open to any other considerations that you wish to add or improve.  Please feel free to contiribute no matter how small the change can you add.

<br><hr><br>

## Important considerations

This is a public repository. Please double-check your commits before pushing:
  - Update documentation if your change introduces new functionality.
  - Add proper `.gitignore` rules to avoid uploading temporary or sensitive files.
  - Never Commit Tokens, Passwords, or Any Credential/Secrets. (or if you commit it for nice examples/references please add `#FAKE` in the end)
  - Run linting/formatting tools to keep code style consistent.
  - If your change affects logic, include or update tests.
  - Do not push large binaries or auto-generated files unless they are explicitly required.
  - Always link your contributions to an existing issue when possible.


<br><hr><br>

### 1. Format names and branching
	
#### Format: 
      <type>/<short-description>
      <type>/<issue-number>

#### Examples:

<ul>
  <li>feat/webserver-refactor</li>
  <li>fix/login-bug</li>
  <li>docs/update-readme</li>
  <li>fix/issue-43</li>
  <li>feat/issue-135</li>
</ul>



<br><hr><br>

### 2. Commits (Conventional Commits)

#### Format:
		<type>(<scope>): <mensaje> [opcional: (#issue)]


| name      | desc                                                    |
|---        |---                                                      |
| type: 		| commit type.                                            |
| scope: 	| module/area/app affected.                               |
| mensaje: 	| small descripción (always in lowercase).                |
| (#issue): | Github Issue reference (optional but super useful).     |


#### Issue type:	

| name           | desc                             |
|---             |---                               |
| feat:          | New functionality (Bump Minor).  | 
| fix:           | BUG correction (Bump Patch).     |
| refactor:      | Code refactorization.            |
| doc/docs:      | Documentation.                   |
| chore:         | maintenance tasks.               |
| test:          | changes or aggregates of tests.  |

#### Examples:
      git commit -m "feat(auth): new login super cool (#43)"
      git commit -m "fix(ui): small correction in css file (#128)"
      git commit -m "refactor(webserver): new architecture (#43)"
      git commit -m "docs(readme): add new document how to do..."

#### Breaking changes:
When an Commit introduces an incompatible change, it must be used! or the Breaking Change text: if you want to be more specific
      
      git commit -m "feat!: change all api functionality (#200)"
      git commit -m "fix(auth)!: delete legacy support (#199)"
      git commit -m "feat(api): change contract (#200)" -m "BREAKING CHANGE: old API removed"

			
<br><hr><br>

### 3. Automatic versioning

This repository uses Semantic Version to generate automatic versions based on commitments, for this reason we will use minimal rules so that everything has coherence.

| Commit                                   | Impact in versión        |
|------------------------------------------|--------------------------|
| feat:                                    | minor)                   |
| fix:                                     | patch)                   |
| feat!: / fix!: / BREAKING CHANGE:        | major)                   |
| chore: / docs: / refactor: / test:       | no changes               |
| feat(api): ... -beta                     | prerelease X.Y.Z-beta    |
| build:                                   | add metadata +sha     	  |

#### Examples

| Ejemplo de commit                         | Versión resultante    |
|-------------------------------------------|-----------------------|
| feat(auth): agregar login (#43)           | 1.3.0                 |
| fix(ui): corregir botón (#44)             | 1.2.4                 |
| feat!: eliminar endpoint legacy (#45)     | 2.0.0                 |
| feat(auth): login social -beta            | 1.3.0-beta            |
| build(docker): optimizar imagen           | 1.2.3+build.a1b2c3    |


<br><hr><br>

### 4. Basic flow


#### Clone or pull 
      git clone ...  or   git pull

#### Make branch from main:
      git checkout -b feat/webserver-refactor

#### Make commits with standard ConvCommits:
      git commit -m "refactor(webserver): new architecture (#43)"

#### Create a PR with standard format:
      refactor(webserver): new architecture (#43)
