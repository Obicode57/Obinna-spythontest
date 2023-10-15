from bs4 import BeautifulSoup
from collections import Counter
import psycopg2
import random
import statistics


html_content = """
<html>
[<head>
<title>Our Python Class exam</title>
<style type="text/css">
	
	body{
		width:1000px;
		margin: auto;
	}
	table,tr,td{
		border:solid;
		padding: 5px;
	}
	table{
		border-collapse: collapse;
		width:100%;
	}
	h3{
		font-size: 25px;
		color:green;
		text-align: center;
		margin-top: 100px;
	}
	p{
		font-size: 18px;
		font-weight: bold;
	}
</style>

</head>
<body>
<h3>TABLE SHOWING COLOURS OF DRESS BY WORKERS AT BINCOM ICT FOR THE WEEK</h3>
<table>
	
	<thead>
		<th>DAY</th><th>COLOURS</th>
	</thead>
	<tbody>
	<tr>
		<td>MONDAY</td>
		<td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td>
	</tr>
	<tr>
		<td>TUESDAY</td>
		<td>ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE</td>
	</tr>
	<tr>
		<td>WEDNESDAY</td>
		<td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE</td>
	</tr>
	<tr>
		<td>THURSDAY</td>
		<td>BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td>
	</tr>
	<tr>
		<td>FRIDAY</td>
		<td>GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE</td>
	</tr>

	</tbody>
</table>

<p>Examine the sequence below very well, you will discover that for every 1s that appear 3 times, the output will be one, otherwise the output will be 0.</p>
<p>0101101011101011011101101000111 <span style="color:orange;">Input</span></p>
<p>0000000000100000000100000000001 <span style="color:orange;">Output</span></p>
<p>
</body>]
</html>
"""
soup = BeautifulSoup(html_content, 'html.parser')

# Find all table rows (tr)
rows = soup.find_all('tr')


monday_colors = None
tuesday_colors= None
wednesday_colors= None
thursday_colors= None
friday_colors = None

# make a loop
for row in rows:
    day_cell = row.find('td')
    if day_cell and day_cell.text.strip() == 'MONDAY':
        # colors for Mon
        monday_colors = row.find_all('td')[1].text.strip()
    if day_cell and day_cell.text.strip() == 'TUESDAY':
        # colors for Tue
        tuesday_colors = row.find_all('td')[1].text.strip()
    if day_cell and day_cell.text.strip() == 'WEDNESDAY':
        # colors for Wed
        wednesday_colors = row.find_all('td')[1].text.strip()
    if day_cell and day_cell.text.strip() == 'THURSDAY':
        # colors for Thur
        thursday_colors = row.find_all('td')[1].text.strip()
    if day_cell and day_cell.text.strip() == 'FRIDAY':
        # colors for Fri
        friday_colors = row.find_all('td')[1].text.strip()
data= (monday_colors + tuesday_colors + wednesday_colors +thursday_colors + friday_colors)
new_data= data.split(',')
print(new_data)




sorted_data= sorted(new_data)

# 1. mean string
mean_string = sorted_data[len(sorted_data) // 2]

print("Mean String (Lexicographic Mean):", mean_string)

# MEAN COLOR IS GREEN

#2. THE MOST COMMON COLOR
color_counts = Counter(new_data)
most_frequent_color = color_counts.most_common(1)[0][0]
print(f'the most frequently worn color is {most_frequent_color}')
#  the most frequently worn color is blue

# 3. MEDIAN
median_= statistics.median(sorted_data)
print(f'The median is {median_}')
# OR
median2_=(sorted_data[45])
print(f'The median is {median2_}')


# 5. the probability of RED
red_count=  data.count('RED')
total_data = len(sorted_data)
red_prob= (red_count/total_data)
print(f'the probaility of red is {red_prob}')
# RED PROBABILITY IS 0.0989

#6.
def postswl():
    while True:
        conn = psycopg2.connect(database="your_database", user="your_user", password="your_password", host="your_host", port="5432")
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE color_frequencies (
            color VARCHAR(50) PRIMARY KEY,
            frequency INT
        )
    """)
        conn.commit()
        color_frequencies = {color_counts}
        for color, frequency in color_frequencies.items():
            cur.execute("INSERT INTO color_frequencies (color, frequency) VALUES (%s, %s)", (color, frequency))
            conn.commit()
            cur.close()
            conn.close()
    return 0
# I am returning 0 because i do not an sql and i dont want the code to error out




#8.  Generate 4 random numbers of 1 or 0
random_numbers = [random.randint(0, 1) for _ in range(4)]
print("Generated random numbers:", random_numbers)
binaryno = ''.join(map(str, random_numbers))
print(binaryno)
decimal= int(binaryno,2)
print(decimal)

# 9. Finnobaci SERIES:
def fibonacci_series(n):
    sequence = [0, 1]

    # Generate the Fibonacci series up to n terms
    while len(sequence) < n:
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)

    return sequence

# Specify the number of terms in the Fibonacci series
num_terms = 50

# Generate the Fibonacci series
fibonacci_series_result = fibonacci_series(num_terms)

print("Fibonacci Series ({} terms):".format(num_terms))
print(fibonacci_series_result)








