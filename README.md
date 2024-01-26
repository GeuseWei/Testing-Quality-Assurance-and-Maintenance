# Skeleton repository for STQAM

All code for the course will be distributed through this repository. 

Each student/group also has a personal repository to submit their work. 
The location of student repository is at

  https://git.uwaterloo.ca/stqam-1239/class/<USERID>

where <USERID> is the student gitlab user id (usually the same as Quest user id)

## Initial setup instructions

```
$ git clone https://git.uwaterloo.ca/stqam-1239/class/<USERID> stqam
$ cd stqam
$ git remote add upstream https://git.uwaterloo.ca/stqam-1239/skeleton
$ git fetch upstream
$ git checkout -b main origin/main
$ git merge upstream/main
$ git push origin main
```

# Fetch new changes from the skeleton (upstream)

```
$ cd stqam
$ git fetch upstream
$ git merge upstream/main
$ git push origin main
```

# Submit completed assignment

```
$ cd stqam
$ git push origin main
```

Make sure to check that the changes are properly submitted online by following 
https://git.uwaterloo.ca/stqam-1239/class/<USERID> with your web browser.

