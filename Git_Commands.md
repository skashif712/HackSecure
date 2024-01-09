This Gist contains all the useful commands for Git
Build Status

Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later.

If you are a developer and want to keep every version of your code/project (which you would most certainly want to), a Version Control System (VCS) is a very wise thing to use.

All the commands used for Git
Compatibility with GitHub

Commands
Set global username and email for Git (Locally).

git config --global user.name "<your username>"
git config --global user.email "<your email>"


git init >>>>  Initialise an empty Git Repository
 
git clone <repository URL> >>>>  Clone an existing Git Repository

git add <filename> >>>>> >  Add file/stage to git

git add .  >>>>>  Add all the files to git

git commit -m "<your commit message>"   >>Commit all the staged files to git

git restore <filename>  >>>> Restore the file from being modified to Tracked
git checkout <filename>  >>>>>> 

git status >>>>  Show the status of your Git respository


git branch  >>> Show the branches of your git repository

git checkout -b <branch name>   >>>Checkout to a new branch



git checkout <branch name>  >>> Checkout to an existing branch

git branch -d <branch name>   >>>>>Remove a branch from Git

git remote -v >>>>Show remote origin URL


git remote add origin <your remote git URL>   >>>>Add remote origin URL


git remote remove origin   >>>>Remove remote origin URL

git fetch >>>>Fetch all the remote branches


git push origin <branch name>   >>>Push your local changes to remote branch

git pull origin <branch name> >>>>Pull your remote changes to local branch

git log   >>>>Check you git commits and logs
