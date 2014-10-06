# Using Git for The Pair Programming Club
## Laura (starrymirth)

Git is a really great version control tool, it's very powerful and flexible, but
that does mean that sometimes it can be a little bit confusing to the beginner. 
There are great tutorials online (including the book http://git-scm.com/book), 
but this will be a reference document for the git commands that we will use most often. 

### Setting up an account on GitHub: 

Pop over to (https://github.com) and make an account (username, email and password).
Note that it will be public, and all projects will be public. If you need to work on something for SANSA, there is an internal GitLab server (talk to Herman for more information) or if you're working on your own stuff I recommend Atlassian Bitbucket, which allows you to have Private projects for very small groups. (Bitbucket also allows you to use Mercurial (`hg`) if you don't like `git`) 

Once you have an account head over to the pair programming repository on my account
(https://github.com/starrymirth/PairProgramming), and click the `Fork` button in the top right hand corner. This will take you to your own 'copy' of the repository, which you can edit freely. 

**NOTE:** There seems to be a bit of an issue with Firefox cache on Linux machines which prevents the Fork from working correctly. If you get to a page that asks you which repository to fork to, and it doesn't let you click the button, either try using Chrome, or clear Firefox's cache by going to `Menu>Preferences>Advanced>Network` and clicking the `Clear Now` button under `Cached Web Content`.

### Common Commands

#### `git clone`
When you first want to get the code from GitHub you need to use `git clone`. If you're working on the lab machines we will use HTTPS, so on the page from GitHub at the bottom right you will see a "HTTPS clone URL" (if it says SSH click the HTTPS button).

You can then run from the terminal the command and that URL, which will be in the form: 

 `git clone https://github.com/<username>/<repository_name>.git`

That will create a folder the same name as the repository into the folder you are in.


#### `git status`
Use this command all the time when you want to see what's going on. It will tell you what is changed, what is staged, and what is pushed to the server.

#### `git pull`
If there have been other changes to the repository that were not on your computer but are on the server, you need to `pull` them from the server, with `git pull`. The default is to pull from your origin, which is the GitHub server, so you don't need to tell it where to pull from. 

#### `git add`
When you add or modify a file, you need to add to to the staging area, (basically tell git that you care about that file and you want the changes to happen when you commit). Use `git add <filename>`

#### `git commit`
This will make a package of all your changes, and you need to give a message basically summarising what you changed. If you say `git commit`, it will open a editor to write your message, but you can do it easier by just typing `git commit -m "<your message here>"`


#### `git push`
This does the opposite of pull, which is to push your changes to the server. If someone has been editing the server, it will prevent you from doing this. You can simply run `git push`, but if your machine is not configured correctly it may give a warning. That is ok, but if you want to get into the habit you can run `git push origin master` which is explicit, saying that we want to push to the `origin` and we want to push the `master` branch. 




