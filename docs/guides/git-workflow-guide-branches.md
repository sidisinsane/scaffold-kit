# Git Workflow Guide: Branches

This guide walks you through the branch workflow in Git, from creating a branch
to cleaning up after merging.

## 1. Create and Set Up a Branch

1. **Ensure you're on the latest main branch**:

```bash
git checkout main
git pull origin main  # Get the latest changes
```

2. **Create a branch**:

```bash
git checkout -b <type>/<description> # e.g., feature/add-init-method

# release branch
git checkout -b release/<MAJOR.MINOR.PATCH> # e.g., release/1.0.1
```

**Branch Naming Conventions**:

| Type       | Purpose                  | Example                        |
| ---------- | ------------------------ | ------------------------------ |
| `bugfix`   | For bug fixes.           | `bugfix/fix-slug-bug`          |
| `chore`    | For non-code tasks.      | `chore/add-git-workflow-guide` |
| `feature`  | For new features.        | `feature/add-init-method`      |
| `hotfix`   | For urgent fixes.        | `hotfix/apply-security-patch`  |
| `refactor` | For code improvements.   | `refactor/change-api-factory`  |
| `release`  | For release preparation. | `release/1.0.1`                |
| `test`     | For new tests.           | `test/add-init-unit-test`      |

3. **Verify you're on the correct branch**:

```bash
git branch
```

The current branch will be marked with an asterisk (\*).

## 2. Develop and Push a Branch

1. **Add changes and commit regularly**:

```bash
git add .
git commit -m "<type>: <description>"
# e.g., "bugfix: Fix slug bug"
```

2. **Push the branch**:

```bash
git push origin <type>/<description>
```

For the first push, Git may suggest using
`git push --set-upstream origin <type>/<description>`.

## 3. Merge a Branch

1. **Update local main branch**:

```bash
git checkout main
git pull origin main
```

2. **Merge the branch**:

```bash
git merge <type>/<description>
```

3. **Push the merged changes**:

```bash
git push origin main
```

4. **Handle merge conflicts**:

   - Git will mark conflicted files
   - Edit the files to resolve conflicts
   - Stage the resolved files: `git add .`
   - Complete the merge: `git commit`

## 4. Clean Up After Merging

After successfully merging, clean up your branches to keep your repository
organized.

1. **Delete a local branch**:

```bash
git branch -d <type>/<description>
```

Use `-D` instead of `-d` if you need to force delete an unmerged branch.

2. **Delete a remote branch**:

```bash
git push origin --delete <type>/<description>
```

Note: If you merged via GitHub's interface, it may offer to delete the branch
automatically.

3. **Verify the cleanup**:

```bash
git branch -a  # List all branches including remotes
```

## Common Issues

- **Merge conflicts**: Use `git status` to see conflicted files, resolve
  manually, then `git add` and `git commit`
- **Wrong branch**: Use `git checkout main` to switch back, then
  `git checkout -b correct-branch-name`
- **Need to update branch**: While on your branch, run `git pull origin main` to
  bring in latest changes
