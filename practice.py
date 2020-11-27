{
 "metadata": {
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4-final"
  },
  "orig_nbformat": 2,
  "kernelspec": {
   "name": "python3",
   "display_name": "Python 3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2,
 "cells": [
  {
   "source": [
    "### Assignment\n",
    "\n",
    "Suppose there is a hat containing 5 blue balls, 4 red balls, and 2 green balls. What is the probability that a random draw of 4 balls will contain at least 1 red ball and 2 green balls? While it would be possible to calculate the probability using advanced mathematics, an easier way is to write a program to perform a large number of experiments to estimate an approximate probability.\n",
    "\n",
    "For this project, you will write a program to determine the approximate probability of drawing certain balls randomly from a hat. \n",
    "\n",
    "First, create a `Hat` class in `prob_calculator.py`. The class should take a variable number of arguments that specify the number of balls of each color that are in the hat. For example, a class object could be created in any of these ways:\n",
    "```\n",
    "hat1 = Hat(yellow=3, blue=2, green=6)\n",
    "hat2 = Hat(red=5, orange=4)\n",
    "hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)\n",
    "```\n",
    "\n",
    "A hat will always be created with at least one ball. The arguments passed into the hat object upon creation should be converted to a `contents` instance variable. `contents` should be a list of strings containing one item for each ball in the hat. Each item in the list should be a color name representing a single ball of that color. For example, if your hat is `{\"red\": 2, \"blue\": 1}`, `contents` should be `[\"red\", \"red\", \"blue\"]`.\n",
    "\n",
    "The `Hat` class should have a `draw` method that accepts an argument indicating the number of balls to draw from the hat. This method should remove balls at random from `contents` and return those balls as a list of strings. The balls should not go back into the hat during the draw, similar to an urn experiment without replacement. If the number of balls to draw exceeds the available quantity, return all the balls.\n",
    "\n",
    "Next, create an `experiment` function in `prob_calculator.py` (not inside the `Hat` class). This function should accept the following arguments:\n",
    "* `hat`: A hat object containing balls that should be copied inside the function.\n",
    "* `expected_balls`: An object indicating the exact group of balls to attempt to draw from the hat for the experiment. For example, to determine the probability of drawing 2 blue balls and 1 red ball from the hat, set `expected_balls` to `{\"blue\":2, \"red\":1}`.\n",
    "* `num_balls_drawn`: The number of balls to draw out of the hat in each experiment.\n",
    "* `num_experiments`: The number of experiments to perform. (The more experiments performed, the more accurate the approximate probability will be.)\n",
    "\n",
    "The `experiment` function should return a probability. \n",
    "\n",
    "For example, let's say that you want to determine the probability of getting at least 2 red balls and 1 green ball when you draw 5 balls from a hat containing 6 black, 4 red, and 3 green. To do this, we perform `N` experiments, count how many times `M` we get at least 2 red balls and 1 green ball, and estimate the probability as `M/N`. Each experiment consists of starting with a hat containing the specified balls, drawing a number of balls, and checking if we got the balls we were attempting to draw.\n",
    "\n",
    "Here is how you would call the `experiment` function based on the example above with 2000 experiments:\n",
    "\n",
    "```\n",
    "hat = Hat(black=6, red=4, green=3)\n",
    "probability = experiment(hat=hat, \n",
    "                  expected_balls={\"red\":2,\"green\":1},\n",
    "                  num_balls_drawn=5,\n",
    "                  num_experiments=2000)\n",
    "```\n",
    "\n",
    "Since this is based on random draws, the probability will be slightly different each time the code is run.\n",
    "\n",
    "*Hint: Consider using the modules that are already imported at the top of `prob_calculator.py`.*\n",
    "\n",
    "### Development\n",
    "\n",
    "Write your code in `prob_calculator.py`. For development, you can use `main.py` to test your code. Click the \"run\" button and `main.py` will run.\n",
    "\n",
    "### Testing \n",
    "\n",
    "The unit tests for this project are in `test_module.py`. We imported the tests from `test_module.py` to `main.py` for your convenience. The tests will run automatically whenever you hit the \"run\" button.\n",
    "\n",
    "### Submitting\n",
    "\n",
    "Copy your project's URL and submit it to freeCodeCamp.\n"
   ],
   "cell_type": "markdown",
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 203,
   "metadata": {},
   "outputs": [],
   "source": [
    "A = [250,\n",
    "\"1/3/2012 16:00:00   27.47\",\n",
    "\"1/4/2012 16:00:00   Missing_1\",\n",
    "\"1/5/2012 16:00:00   27.728\",\n",
    "\"1/6/2012 16:00:00   28.19\",\n",
    "\"12/13/2012 16:00:00   27.52\",\n",
    "\"12/14/2012 16:00:00   Missing_19\",\n",
    "\"12/17/2012 16:00:00   27.215\",\n",
    "\"12/18/2012 16:00:00   27.63\",\n",
    "\"12/19/2012 16:00:00   27.73\",\n",
    "\"12/20/2012 16:00:00   Missing_20\",\n",
    "\"12/21/2012 16:00:00   27.49\",\n",
    "\"12/24/2012 13:00:00   27.25\",\n",
    "\"12/26/2012 16:00:00   27.2\",\n",
    "\"12/27/2012 16:00:00   27.09\",\n",
    "\"12/28/2012 16:00:00   26.9\",\n",
    "\"12/31/2012 16:00:00   26.77\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 185,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "27.81\n27.29\n27.28\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "from sklearn.linear_model import LinearRegression\n",
    "from datetime import datetime\n",
    "results = A[1:]\n",
    "first_day = datetime.strptime(A[1].split(\" \")[0],'%m/%d/%Y')\n",
    "date =[]\n",
    "tem =[]\n",
    "missing = []\n",
    "for result in results:\n",
    "    days_text = result.split(\"  \")[0].split(\" \")[0]\n",
    "    days_text = days_text.split(\"/\")[0].rjust(2,\"0\")+\"-\" + days_text.split(\"/\")[1].rjust(2,\"0\") + \"-\" + days_text.split(\"/\")[2]\n",
    "    days = (datetime.strptime(days_text, '%m-%d-%Y') - first_day).days\n",
    "    \n",
    "    if result.split()[2].find(\"Missing\") ==-1:\n",
    "        tem.append(float(result.split()[2].strip()))\n",
    "        date.append(days)\n",
    "    else:\n",
    "        missing.append(days)\n",
    "Model = LinearRegression()\n",
    "X = np.array(date).reshape(-1,1)\n",
    "Y = np.array(tem).reshape(-1,1)\n",
    "Model.fit(X,Y)\n",
    "alpha = Model.intercept_[0]\n",
    "beta = Model.coef_[0][0]\n",
    "for i in missing:\n",
    "    number = round(float(alpha + beta *i),2)\n",
    "    print(number)\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 204,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "[27.47, 27.52, 27.73]\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "from datetime import datetime\n",
    "results = A[1:]\n",
    "first_day = datetime.strptime(A[1].split(\" \")[0],'%m/%d/%Y')\n",
    "date =[]\n",
    "tem =[]\n",
    "missing = []\n",
    "for result in results:\n",
    "    days_text = result.split(\"  \")[0].split(\" \")[0]\n",
    "    days_text = days_text.split(\"/\")[0].rjust(2,\"0\")+\"-\" + days_text.split(\"/\")[1].rjust(2,\"0\") + \"-\" + days_text.split(\"/\")[2]\n",
    "    days = (datetime.strptime(days_text, '%m-%d-%Y') - first_day).days\n",
    "    date.append(days)\n",
    "    if result.split()[2].find(\"Missing\") ==-1:\n",
    "        tem.append(float(result.split()[2].strip()))\n",
    "        missing.append(0)\n",
    "        \n",
    "    else:\n",
    "        tem.append(np.nan)\n",
    "        missing.append(1)\n",
    "result = {\"date\":date,\"tem\":tem,\"missing\":missing}\n",
    "result_total = pd.DataFrame(result)\n",
    "result_total[\"tem\"] = result_total[\"tem\"].fillna(method='pad',limit=1)\n",
    "result_total[\"tem\"] = result_total[\"tem\"].fillna(method='bfill',limit=1)\n",
    "A = result_total[\"tem\"][result_total[\"missing\"] ==1].tolist()\n",
    "print(A)\n",
    "\n"
   ]
  }
 ]
}