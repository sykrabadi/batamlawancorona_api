## How To Contribute?
We love any works you do for this repository. You can contribute to this repository by doing :
- Reporting bugs
- Code review
- Submitting a fix
- Suggests new features
- Become maintainer

## Contribution Guideline
1. Fork this repository and clone it to your computer
2. Create Python virtual environment, by typing `python -m venv venv` in your terminal/cmd
3. Create a new branch from the `main` branch and checkout your newly created branch
4. Install the required packages that stored at requirements.txt file by typing `pip install -r requirements.txt` in your terminal/cmd
5. After the packages has successfully installed, run migrations for the first time by typing `python manage.py makemigrations`, and finalize the migrations by typing `python manage.py migrate`
in your terminal/cmd
6. Open `settings.py` file that lies on `batamlawancorona_api` folder. Look for `DEBUG` variable, and set the value to `TRUE`
7. Run the project by typing python `manage.py runserver` in your terminal/cmd
8. Create and commit your changes
9. Push your commit to the forked repository on your GitHub
10. Create a Pull Request by comparing your new branch to the `main` branch
