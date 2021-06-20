
# 00 Getting Started

#### HuStar Robot Academy

Lecture Notes by idebtor@gmail.com
-------------------
  __To get started__, do the first thing first:

  1. Read Syllabus or README if any.
  2. Read 'GettingStarted' - this file
  3. Follow instructions in 'GettingStarted' as soon as possible(ASAP).

  These reading materials is available at my [github.com/idebtor/HuStarML](https://github.com/idebtor/HuStarML).

### How to view markdown(.md) files in Chrome (or rendering in HTML)
  0. View them always in github website automatically and better.
  - and/or
  1. Install `Markdown Viewer` extension.
  2. Navigate to `chrome://extensions` and
      - Locate `Markdown Viewer` and click on the `DETAILS` button
      - Check the option `Allow access to file URLs`
  2. 크롬에서 `chrome://extensions` 접속 한 후,
      - `Markdown Viewer` `세부정보`에서
      - "파일 URL에 대한 액세스 허용"을 체크하십시오
  3. Open local or remote .md file in Chrome.
  4. Enjoy nicely formatted HTML!

-----------------------------------
## Install "GitHub Desktop" and "Git"
- Install __git__ from [this site](https://git-scm.com/downloads) for your computer.
- Install __GitHub Desktop__

After installation of GitHub Desktop, be a member if already not.
  - Clone the GitHub `HuStar` repository into your local computer:
    - https://github.com/idebtor/HuStar  
  - __How to clone a repository from GitHub:__ Refer to [this site](https://help.github.com/desktop/guides/contributing-to-projects/cloning-a-repository-from-github-desktop/).
  - Click __'watch'__ and __'star'__ at the top of the web page.
  - Then, in your computer, you may have the following `github/HuStar` folder as shown below:

  ```
  C:\GitHub\HuStar
  ```
  - Since this `HuStar` repository can be updated anytime, keep this local repository as "read-only".  Don't code yours here!.
  - Copy them into your own repository or your own local development folders in your computer you can easily access them.  They should look like the following:

  ```
    ~/HuStarML          # Machine Learning
    ~/HuStarAS          # Android Studio
  ```
__Note for Multi-screen users:__ Remove the following file if GitHub Desktop is displayed off-screen. Restart Desktop GitHub. (`user` below may be different in your system.)
```
C:\Users\user\AppData\Roaming\GitHub Desktop\window-state.json
```

__JoyNote__: How do I force `git pull` to overwrite local files?

- Go to the ~/HuStarML folder.
- Open a console and run the following two commands.

```
git fetch --all
git reset --hard origin/master
```
or
```
git stash
```

__Explanation:__ `git fetch` downloads the latest from remote without trying to merge or rebase anything. Then the `git reset` resets the master branch to what you just fetched. The `--hard` option changes all the files in your working tree to match the files in origin/master

__Caution:__ If you have any local changes, they will be lost. With or without --hard option, any local commits that haven't been pushed will be lost.

__JoyNote__: How do I keep my local files clean after trials?
- Go to the ~/HuStarML folder.
- Open a console and run the following command.
```
git clean -f
```
__Explanation:__ To delete all untracked files.



## Install Anaconda
Anaconda is  a Python and R distribution package. It aims to provide everything you need (python wise) for data science "out of the box".  It includes:
-	The core python language
-	200+ python "packages" (libraries)
-	Spyder (IDE/editor) and Jupyter Notebook
-	conda, Anaconda's own package manager, used for updating Anaconda and packages

#### To install the anaconda:

  - Visit website [Anaconda Distribution](https://www.anaconda.com/distribution/)
    - Choose one of Windows/MacOS/Linux
    - Python 3.x Version Download
  - At the beginning of installation, check the following option
      - Add Anaconda to my PATH environment variable as shown below:

<p align="center"> <img src="https://github.com/idebtor/KMOOC-ML/blob/master/ipynb/images/anaconda_check_path.png" width=400"> </p>

  - Need help? Follow [this guide](https://m.blog.naver.com/PostView.nhn?blogId=jooostory&logNo=221196479998&proxyReferer=https%3A%2F%2Fwww.google.com%2F).

#### After your installation
Do the following in cmd windows or in PowerShell to check your successful installation; ($ is just a prompt of your console, >>> is a prompt from Python.)

      ```
      $ python
      >>> import tensorflow as tf
      >>> print(tf.__version__)
      2.3.0
      >>> import keras
      Using TensorFlow backend
      ```

## Install Code or Install Atom - THE editor for coders
1. Either Code or Atom is a text editor that most professional coders love nowadays.
2. Start Atom or Code.
3. For Atom, install some of essential packages recommended for C/C++ programmers listed below:

    - File-icons
    - Minimap
    - Markdown-preview
      - Open a rendered version of the Markdown in the current editor with `ctrl-shift-m`.
    - Autosave
      - It automatically saves files when the editors loses focus, are destroyed, or when the window is closed. Believe or not, it is disabled by default. __You must check `enabled`__ in config setting or from the Autosave section of the Settings view.

    __Themes of my personal preference__:
      - UI Theme - Atom Dark,
      - Syntax Theme - Oceanic Next

    __Note for Multi-screen users:__ If Atom is displayed off-screen, do the following:
      1. Alt + Tab to choose the atom window
      2. Alt + Space to open the context menu
      3. Press 'm' to select move
      4. Press any arrow key once
      5. Move your mouse (The misplaced window will follow your cursor.)

      Alternatively, remove the following file: [`user` is your login name]
        ```
        C:\Users\user\AppData\Roaming\GitHub Desktop\window-state.json
      ```

    __Problem in platformio-ide-terminal:__ If the prompt does not show up in the terminal, you may look Issues #765 and #760 at github/platformio/platformio-atom-ide-terminal.
      1. #760 is a solution for Windows users.
      2. #765 includes a comment I posted. What I found is to follow the #760 solution except one item. Use apm instead of npm.

#### Need more installation?
Use the following command if you need more installation of packages (-U for upgrade only):
  ```
  $ pip install a_package_name
  $ pip install -U a_package_name              
  ```

### How to view Jupyter Notebook files(.ipynb) in a browser

0. View them in github website automatically, but cannot run the code cells.
and/or
1. Follow the instructions [here](https://jupyter.readthedocs.io/en/latest/install.html) to install Python and Jupyter Notebook.
2. Open a console, run the following command to run the Jupyter notebook
```
 $ jupyter notebook
```
or double-click the following file on pc if available
```
$ _start_ipynb.bat
```
3. Now, you can read, run and edit the code/markdown cells.
----------------------------
_One thing I know, I was blind but now I see. John 9:25_

----------------------------
