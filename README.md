# `RanTool` : A `PsychoPy` script to measure the ability to produce random series

This is a `python` based script to conduct simple experiments on human-generated randomness. It allows to gather basic demographic data like: sex, age, faculty and dominant 
hand. First it displays two intructions and afterward a red square which dictates the tempo of random series generation. It allows to only gather reposnses from two keys 
('perion' and 'slash') but an easy modification might change it. It writes all the data to a `csv` format file. During the process of generating randomness the scrip allows to
display the history of already produced elements. Therefore, it allows to run experiments in which in one condition participants last generated elements and in the second 
condition they do not see them.

The main script `ranTool.py` reads infomration about the condition from `conditions.csv` file which might be created with the use of `make_conditions.py` python script. By 
defualt `make_conditions.py` created a random list of 50 visible history and 50 invisible history condition.

## Main Dependencies

