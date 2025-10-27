# 🚀 GitHub Mastery: 6-Week Complete Course

## 📋 Course Overview

**Duration:** 6 Weeks (3 sessions per week, 2 hours each)  
**Total Hours:** 36 hours  
**Level:** Beginner to Intermediate  
**Prerequisites:** Basic computer skills, command line familiarity (helpful but not required)

---

## 🎯 Learning Objectives

By the end of this course, students will be able to:
- Create and manage GitHub repositories
- Use Git for version control effectively
- Collaborate with teams using branches and pull requests
- Resolve merge conflicts confidently
- Implement GitHub Actions for CI/CD
- Build a professional portfolio using GitHub Pages
- Contribute to open-source projects

---

## 📚 Course Structure

### **Week 1: Git & GitHub Fundamentals**

#### **Session 1.1: Introduction to Version Control (2 hours)**
**Topics:**
- What is version control and why it matters
- Git vs GitHub: Understanding the difference
- Setting up Git (installation, configuration)
- Creating a GitHub account
- Understanding repositories

**Hands-On Activities:**
1. Install Git on local machine
2. Configure Git (username, email)
3. Create first GitHub account
4. Explore existing open-source repositories
5. Create your first repository (web interface)

**Commands Covered:**
```bash
git --version
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
git config --list
```

**Homework:**
- Create a personal repository called "learning-github"
- Add a README.md file describing your learning goals
- Read: GitHub's "Hello World" guide

---

#### **Session 1.2: Basic Git Operations (2 hours)**
**Topics:**
- Git workflow: Working Directory → Staging → Repository
- Basic Git commands (add, commit, status, log)
- Writing good commit messages
- The .gitignore file
- Viewing history

**Hands-On Activities:**
1. Clone the "learning-github" repository
2. Create and modify files
3. Stage and commit changes
4. View commit history
5. Create a .gitignore file

**Commands Covered:**
```bash
git clone <url>
git status
git add <file>
git add .
git commit -m "message"
git log
git log --oneline
git diff
```

**Lab Exercise:**
Create a simple "My Portfolio" project:
- Create index.html, style.css, about.md
- Make at least 5 commits with meaningful messages
- Use .gitignore to exclude unnecessary files

**Homework:**
- Complete the portfolio project
- Practice 10 commits with descriptive messages
- Read about commit message best practices

---

#### **Session 1.3: Connecting Local & Remote (2 hours)**
**Topics:**
- Remote repositories explained
- Push, pull, and fetch operations
- SSH vs HTTPS authentication
- Setting up SSH keys
- Understanding origin and remote

**Hands-On Activities:**
1. Generate SSH keys
2. Add SSH key to GitHub account
3. Push local repository to GitHub
4. Make changes on GitHub web interface
5. Pull changes to local machine

**Commands Covered:**
```bash
git remote add origin <url>
git remote -v
git push origin main
git push -u origin main
git pull origin main
git fetch
```

**Lab Exercise:**
- Create a "recipes" repository
- Add 3 recipe markdown files locally
- Push to GitHub
- Edit one recipe on GitHub web
- Pull changes back to local

**Homework:**
- Set up SSH authentication
- Create 2 more repositories and practice push/pull
- Document any issues faced

---

### **Week 2: Branching & Collaboration**

#### **Session 2.1: Branching Basics (2 hours)**
**Topics:**
- What are branches and why use them
- Creating and switching branches
- The main/master branch
- Branch naming conventions
- Viewing and managing branches

**Hands-On Activities:**
1. Create feature branches
2. Switch between branches
3. Make changes on different branches
4. View branch structure
5. Delete old branches

**Commands Covered:**
```bash
git branch
git branch <branch-name>
git checkout <branch-name>
git checkout -b <branch-name>
git switch <branch-name>
git branch -d <branch-name>
git branch -a
```

**Lab Exercise:**
Build a "team-website" project:
- Create `main` branch with basic structure
- Create `feature/header` branch for header
- Create `feature/footer` branch for footer
- Create `feature/about-page` branch
- Make commits on each branch

**Homework:**
- Create a project with at least 3 feature branches
- Practice switching between branches
- Document the branch strategy used

---

#### **Session 2.2: Merging Branches (2 hours)**
**Topics:**
- Merging strategies (fast-forward, three-way merge)
- Understanding merge commits
- When to merge vs rebase
- Keeping branches updated
- Merge best practices

**Hands-On Activities:**
1. Merge feature branches into main
2. Practice fast-forward merges
3. Create and merge multiple features
4. View merge history
5. Clean up merged branches

**Commands Covered:**
```bash
git merge <branch-name>
git merge --no-ff <branch-name>
git log --graph --oneline --all
git branch -d <merged-branch>
```

**Lab Exercise:**
Continue "team-website" project:
- Merge `feature/header` into main
- Merge `feature/footer` into main
- Merge `feature/about-page` into main
- Verify all features work together
- Clean up feature branches

**Homework:**
- Create a "blog" project with 4 posts as separate branches
- Merge all branches systematically
- Document merge strategy

---

#### **Session 2.3: Merge Conflicts (2 hours)**
**Topics:**
- What are merge conflicts and why they occur
- Reading conflict markers
- Resolving conflicts manually
- Using merge tools
- Preventing conflicts
- Testing after conflict resolution

**Hands-On Activities:**
1. Intentionally create merge conflicts
2. Identify conflict markers
3. Resolve conflicts manually
4. Complete the merge
5. Verify resolution

**Commands Covered:**
```bash
git merge <branch-name>
git status  # during conflict
git add <resolved-file>
git commit  # complete merge
git merge --abort  # cancel merge
git diff
```

**Lab Exercise - Conflict Resolution:**
1. Create a "config-manager" repo
2. Create two branches that modify the same file differently
3. Merge and resolve conflicts
4. Practice with at least 3 different conflict scenarios
5. Document resolution steps

**Homework:**
- Practice creating and resolving 5 different conflicts
- Write a guide on conflict resolution
- Share experiences with classmates

---

### **Week 3: Advanced Git Techniques**

#### **Session 3.1: Undoing Changes (2 hours)**
**Topics:**
- Difference between reset, revert, and checkout
- Undoing uncommitted changes
- Amending commits
- Reverting commits
- Reset modes (soft, mixed, hard)
- Recovering lost commits (reflog)

**Hands-On Activities:**
1. Undo working directory changes
2. Unstage files
3. Amend last commit
4. Revert a commit
5. Use reset safely
6. Recover "lost" commits

**Commands Covered:**
```bash
git checkout -- <file>
git restore <file>
git reset HEAD <file>
git commit --amend
git revert <commit-hash>
git reset --soft HEAD~1
git reset --mixed HEAD~1
git reset --hard HEAD~1
git reflog
```

**Lab Exercise - Time Travel:**
- Create a project with 10 commits
- Practice amending the last commit
- Revert a middle commit
- Reset to a previous state
- Use reflog to recover a "lost" commit

**Homework:**
- Document all undo operations with examples
- Create a cheat sheet for recovery scenarios
- Practice safe undo operations

---

#### **Session 3.2: Stashing & Cherry-Picking (2 hours)**
**Topics:**
- What is stashing and when to use it
- Stash operations (save, pop, apply, list)
- Cherry-picking commits
- Stash vs commit
- Managing multiple stashes
- Cherry-pick use cases

**Hands-On Activities:**
1. Stash uncommitted changes
2. Switch branches and work
3. Apply stashed changes
4. Cherry-pick specific commits
5. Manage stash list

**Commands Covered:**
```bash
git stash
git stash save "message"
git stash list
git stash pop
git stash apply
git stash drop
git stash clear
git cherry-pick <commit-hash>
```

**Lab Exercise - Workflow Management:**
- Start work on a feature
- Stash changes to fix urgent bug
- Return to feature work
- Cherry-pick a commit from another branch
- Manage multiple stashes

**Homework:**
- Create 3 scenarios where stashing is useful
- Practice cherry-picking 5 different commits
- Document when to use each technique

---

#### **Session 3.3: Rebasing & History Management (2 hours)**
**Topics:**
- Interactive rebase
- Rewriting commit history
- Squashing commits
- Reordering commits
- Rebase vs merge: when to use each
- Golden rule of rebasing

**Hands-On Activities:**
1. Simple rebase operation
2. Interactive rebase to squash commits
3. Reorder commits
4. Edit commit messages
5. Split commits

**Commands Covered:**
```bash
git rebase <branch>
git rebase -i HEAD~3
git rebase -i <commit-hash>
git rebase --continue
git rebase --abort
```

**Lab Exercise - History Cleanup:**
- Create a feature with messy commit history
- Use interactive rebase to:
  - Squash related commits
  - Reorder commits logically
  - Edit commit messages
  - Remove unnecessary commits
- Push cleaned history to a new branch

**Homework:**
- Practice interactive rebase 10 times
- Create before/after examples
- Write blog post on rebase best practices

---

### **Week 4: Collaboration & Pull Requests**

#### **Session 4.1: Forking & Pull Requests (2 hours)**
**Topics:**
- Forking repositories
- Upstream vs origin
- Creating pull requests
- Pull request best practices
- PR templates
- Code review process

**Hands-On Activities:**
1. Fork an existing repository
2. Clone forked repository
3. Create a feature branch
4. Make changes and commit
5. Push to fork
6. Create pull request
7. Address review comments

**GitHub UI Skills:**
- Navigate pull requests
- Use PR comments
- Request reviewers
- Approve/reject PRs
- Merge strategies in GitHub

**Lab Exercise - First Contribution:**
Students work in pairs:
- Student A creates a "class-project" repo
- Student B forks and creates a feature
- Student B submits PR
- Student A reviews and requests changes
- Student B updates PR
- Student A merges PR

**Homework:**
- Find an open-source project and create a PR
- Review 2 classmates' PRs
- Document the PR process

---

#### **Session 4.2: Collaborative Workflows (2 hours)**
**Topics:**
- Git Flow workflow
- GitHub Flow (feature branch workflow)
- Trunk-based development
- Protected branches
- Branch policies
- Team collaboration strategies

**Hands-On Activities:**
1. Set up protected main branch
2. Implement GitHub Flow
3. Practice code reviews
4. Handle concurrent features
5. Resolve integration issues

**GitHub Settings:**
- Branch protection rules
- Required reviews
- Status checks
- CODEOWNERS file
- Issue templates

**Lab Exercise - Team Simulation:**
Groups of 3-4 students:
- Create shared repository
- Set up branch protection
- Each member creates a feature
- Submit PRs simultaneously
- Review each other's code
- Merge features systematically

**Homework:**
- Document your team's workflow
- Create a contribution guide
- Set up branch protection on personal projects

---

#### **Session 4.3: Issues & Project Management (2 hours)**
**Topics:**
- Creating and managing issues
- Issue labels and milestones
- Assigning issues
- Issue templates
- Linking PRs to issues
- GitHub Projects (Kanban boards)
- Automations

**Hands-On Activities:**
1. Create detailed issues
2. Add labels and milestones
3. Assign issues to team members
4. Link PRs to close issues
5. Set up project board
6. Track progress

**Lab Exercise - Project Management:**
Build a "class-management-system":
- Create 15 issues for features
- Organize with labels (bug, enhancement, documentation)
- Set up 3 milestones
- Create project board
- Move issues through workflow
- Close issues via commits/PRs

**Homework:**
- Manage a personal project with issues
- Create comprehensive issue templates
- Set up automated project board

---

### **Week 5: GitHub Advanced Features**

#### **Session 5.1: GitHub Actions - CI/CD Basics (2 hours)**
**Topics:**
- What is CI/CD
- GitHub Actions overview
- Workflows, jobs, and steps
- Triggers (push, PR, schedule)
- Using actions from marketplace
- Secrets management

**Hands-On Activities:**
1. Create first workflow file
2. Set up automated testing
3. Add build process
4. Configure triggers
5. Use marketplace actions

**Lab Exercise - Automated Testing:**
Create a simple Node.js or Python project:
- Write tests
- Create workflow to run tests on push
- Add linting check
- Configure to run on PRs
- Add status badge to README

**Workflow Example:**
```yaml
name: Run Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run tests
        run: npm test
```

**Homework:**
- Set up CI/CD for 2 personal projects
- Explore GitHub Actions marketplace
- Create custom workflow

---

#### **Session 5.2: GitHub Pages & Documentation (2 hours)**
**Topics:**
- GitHub Pages overview
- Static site hosting
- Jekyll basics
- Custom domains
- Documentation sites
- Portfolio creation

**Hands-On Activities:**
1. Enable GitHub Pages
2. Create personal portfolio site
3. Customize Jekyll theme
4. Add custom domain (optional)
5. Create project documentation

**Lab Exercise - Portfolio Website:**
Create professional developer portfolio:
- Set up GitHub Pages
- Choose and customize theme
- Add projects section
- Include resume/CV
- Add contact form
- Make it mobile responsive

**Homework:**
- Complete portfolio website
- Add 3 project showcases
- Share portfolio link with class

---

#### **Session 5.3: Advanced GitHub Features (2 hours)**
**Topics:**
- GitHub Gists
- GitHub Discussions
- Wiki pages
- Release management
- GitHub Sponsors
- GitHub CLI
- Advanced search

**Hands-On Activities:**
1. Create useful gists
2. Set up discussions for project
3. Create wiki documentation
4. Tag and release version
5. Install and use GitHub CLI

**Commands Covered:**
```bash
gh repo clone <repo>
gh pr create
gh pr list
gh pr view
gh issue create
gh issue list
gh repo create
```

**Lab Exercise - Complete Project Setup:**
- Create comprehensive project
- Add discussions
- Create detailed wiki
- Make first release (v1.0.0)
- Set up all documentation
- Use GitHub CLI for operations

**Homework:**
- Set up GitHub CLI
- Create 5 useful gists
- Practice GitHub CLI commands

---

### **Week 6: Real-World Projects & Best Practices**

#### **Session 6.1: Open Source Contribution (2 hours)**
**Topics:**
- Finding projects to contribute to
- Understanding contribution guidelines
- Making your first contribution
- Working with maintainers
- Building reputation
- Hacktoberfest and similar events

**Hands-On Activities:**
1. Find beginner-friendly projects
2. Read CONTRIBUTING.md files
3. Pick an issue to work on
4. Submit real contribution
5. Engage with maintainers

**Resources:**
- Good First Issue websites
- Awesome Lists
- GitHub Explore
- up-for-grabs.net
- firstcontributions.github.io

**Lab Exercise - Real Contribution:**
Each student must:
- Find an open-source project
- Fork and clone it
- Fix a bug or add a feature
- Submit a pull request
- Document the experience

**Homework:**
- Make 3 open-source contributions
- Help classmates with their contributions
- Write reflection on the experience

---

#### **Session 6.2: Team Project (2 hours)**
**Topics:**
- Planning a team project
- Setting up collaboration
- Agile development with GitHub
- Code review practices
- Continuous integration
- Deployment strategies

**Team Project Requirements:**
Groups of 4 students build a web application:
- Use proper Git workflow
- Implement CI/CD
- Practice code reviews
- Use issues for tasks
- Document everything
- Deploy to GitHub Pages or Heroku

**Project Ideas:**
1. Task management app
2. Recipe sharing platform
3. Student grade tracker
4. Expense tracker
5. Portfolio template generator

**Lab Exercise - Project Kickoff:**
- Form teams
- Choose project
- Set up repository
- Create project board
- Assign initial tasks
- Create first features

**Homework:**
- Complete assigned features
- Review teammates' code
- Update project board

---

#### **Session 6.3: Final Presentations & Best Practices (2 hours)**
**Topics:**
- Project presentations
- Best practices review
- Security considerations
- Backup strategies
- Career development with GitHub
- Continuing education

**Activities:**
1. Team presentations (10 minutes each)
2. Code review of projects
3. Best practices discussion
4. Q&A session
5. Course review

**Team Presentations Include:**
- Project overview
- Git workflow used
- Challenges faced
- Solutions implemented
- Lessons learned
- Future improvements

**Best Practices Checklist:**
- ✅ Commit often with clear messages
- ✅ Use branches for features
- ✅ Write good README files
- ✅ Review code before merging
- ✅ Keep main branch stable
- ✅ Use .gitignore properly
- ✅ Secure sensitive data
- ✅ Document your code
- ✅ Test before pushing
- ✅ Contribute to open source

**Final Assessment:**
- Team project evaluation (40%)
- Individual contribution (30%)
- Open-source contribution (15%)
- Portfolio/GitHub profile (15%)

**Course Completion:**
- Certificate of completion
- LinkedIn recommendation
- GitHub profile review
- Career guidance

---

## 📝 Weekly Homework Summary

### Week 1 Homework:
1. Create 3 repositories
2. Practice 20+ commits with good messages
3. Set up SSH authentication
4. Complete portfolio project

### Week 2 Homework:
1. Create project with 5 branches
2. Practice merging workflows
3. Resolve 5 different conflicts
4. Document branching strategy

### Week 3 Homework:
1. Practice all undo operations
2. Create stashing scenarios
3. Perform 10 interactive rebases
4. Write technique documentation

### Week 4 Homework:
1. Submit real open-source PR
2. Review 2 classmates' PRs
3. Set up project board
4. Create issue templates

### Week 5 Homework:
1. Set up CI/CD for 2 projects
2. Complete portfolio website
3. Create 5 useful gists
4. Practice GitHub CLI

### Week 6 Homework:
1. Make 3 open-source contributions
2. Complete team project
3. Polish GitHub profile
4. Prepare presentation

---

## 🛠️ Required Tools & Setup

### Software Installation:
1. **Git** - [Download](https://git-scm.com/downloads)
2. **VS Code** - [Download](https://code.visualstudio.com/)
3. **GitHub CLI** (optional) - [Download](https://cli.github.com/)

### VS Code Extensions:
- GitLens
- GitHub Pull Requests
- Git Graph
- Markdown Preview Enhanced

### Accounts Needed:
- GitHub account (free)
- Email address
- SSH key setup

---

## 📚 Learning Resources

### Official Documentation:
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Docs](https://docs.github.com/)
- [GitHub Learning Lab](https://lab.github.com/)

### Interactive Learning:
- [Learn Git Branching](https://learngitbranching.js.org/)
- [Git Immersion](http://gitimmersion.com/)
- [Visualizing Git](https://git-school.github.io/visualizing-git/)

### Books (Free):
- Pro Git (online)
- Git from the Bottom Up
- Learn Git in a Month of Lunches

### Video Resources:
- GitHub YouTube Channel
- FreeCodeCamp Git tutorials
- Traversy Media Git crash course

---

## 🎯 Assessment Criteria

### Individual Assessment (60%):
- Homework completion (20%)
- Class participation (10%)
- Open-source contribution (15%)
- Portfolio project (15%)

### Team Assessment (40%):
- Project functionality (15%)
- Code quality (10%)
- Git workflow adherence (10%)
- Presentation (5%)

### Bonus Points:
- Helping classmates (+5%)
- Extra open-source contributions (+5%)
- Creating learning resources (+5%)

---

## 🏆 Certification Requirements

To earn certification:
- ✅ Attend 90%+ of sessions
- ✅ Complete all homework
- ✅ Make 3+ open-source contributions
- ✅ Complete team project
- ✅ Maintain active GitHub profile
- ✅ Pass final assessment (70%+)

---

## 💡 Success Tips

### For Students:
1. **Practice daily** - Even 30 minutes helps
2. **Break things** - Best way to learn recovery
3. **Read others' code** - Learn from open source
4. **Ask questions** - No question is stupid
5. **Build portfolio** - Showcase your work
6. **Network** - Connect with other developers
7. **Stay curious** - Explore new features

### For Instructors:
1. **Live demos** - Show real workflows
2. **Pair programming** - Learn together
3. **Real projects** - Make it practical
4. **Encourage mistakes** - Safe environment
5. **Code reviews** - Teach best practices
6. **Guest speakers** - Bring in professionals
7. **Stay updated** - GitHub changes frequently

---

## 📞 Support & Community

### Getting Help:
- Class Slack/Discord channel
- Office hours (twice weekly)
- Study groups
- GitHub Discussions
- Stack Overflow

### Community:
- Class GitHub Organization
- Peer code reviews
- Lightning talks
- Show & tell sessions

---

## 🎓 Next Steps After Course

### Immediate:
- Polish GitHub profile
- Continue open-source contributions
- Build 3 portfolio projects
- Network on GitHub

### Short-term (1-3 months):
- Contribute to larger projects
- Mentor others
- Start a blog about learning
- Attend local meetups

### Long-term (3-6 months):
- Become project maintainer
- Speak at meetups
- Create own open-source project
- Consider GitHub certifications

---

## 📅 Sample Schedule

### Monday: Core Concepts
- Theory and fundamentals
- Command line practice
- Individual exercises

### Wednesday: Collaboration
- Team activities
- Code reviews
- Group discussions

### Friday: Hands-On Labs
- Project work
- Problem-solving
- Q&A sessions

---

## 🎉 Course Completion

Congratulations! You now have:
- ✅ Solid Git fundamentals
- ✅ GitHub collaboration skills
- ✅ CI/CD experience
- ✅ Open-source contributions
- ✅ Professional portfolio
- ✅ Team project experience
- ✅ Industry-ready skills

**Welcome to the GitHub community! 🚀**