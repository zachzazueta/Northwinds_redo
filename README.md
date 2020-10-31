# Northwind_redo

The goal of this project will be to conduct business analysis for Northwind Traders, a ficticious company.

There are a number of business questions that will be assessed:
- Does discount increase the quantity sold enough to be profitable?
- Does discount amount have a statistically significant effect on the quantity of a product in an order? If so, at what level(s) of discount?
- Is there a difference in mean time to ship?
- Is there a difference in products that are ordered by region?

This cleaned version will attempt to optimize the SQL queries - while I utilized Python to join data frames in the first round of analysis, I will use sqlite to manipulate the data first, reducing the code to be run following the queries.

I also explore the possible gross profit margins seen across product categories and breakout the needed increase in quantity sold to match a discount provided given a possible existing profit margin. I estimate that Northwinds will have a gpm between 30-50% on goods sold, however, accessing real COGS would help better target that figure.

## The Data
The data for this project is pulled from a publicly available sqlite database for Northwind Traders. There are a number of tables in the database, and they can be seen here:

![alt text](https://github.com/zachzazueta/Northwinds_redo/blob/master/Northwind.png)

As you can see, there is information about orders, customers, employees, and business related matters (shippers, etc). This is an entirely plausible example of a company's relational database, as it stores key information about business structure and function. Parts that would be nice to see would be tables providing information about the expense side of Northwinds, as this would strengthen business analysis.

## Libraries and queries

Standard libraries - pandas, numpy, seaborn - were used in data cleaning and light visualizations for this project. I also employed the use of sqlite3 to generate SQL queries directly in my Notebooks. I utilize statsmodels and scipy for T Tests, Least Squares regression, and Chi Squared tests.

I also wrote a few functions in a separate file, ProjectFunctions, and import them, showcasing the use of a separate file storage for functions which might be used again in future work.

Below is an example of the use of sqlite3 in Python. A connection object is established to connect to the database. This query is selecting the Quantity, Product Category, Price, and Discount amount of each Product in each Order from 3 tables, and excludes discount levels where the discount was 1%, 2%, 3%, 4%, or 6% of price due to the low occurance of those discount levels.

```
conn = sqlite3.Connection('Northwind_small.sqlite')

od_query = pd.read_sql('''SELECT a.OrderId, a.ProductId, a.UnitPrice, a.Quantity, a.Discount, c.CategoryName 
                          FROM OrderDetail a LEFT JOIN Product b ON a.ProductId = b.ID LEFT JOIN Category c ON b.CategoryId = c.ID
                          WHERE (a.Discount != 0.01 AND a.Discount != 0.02 AND a.Discount != 0.03 AND a.Discount != 0.04 
                          AND a.Discount != 0.06)''', conn)

df = pd.DataFrame(od_query)
```

After conducting an ANOVA test to determine that there was evidence to reject the null hypothesis (H0 = discount has no impact on quantity sold), for each product group I calculated the difference in mean quantity sold per order at each discount amount [5%, 10%, 15%, 20%, 25%] compared to a 0% discount.

Lite research suggested that food wholesellers will see profit margins between 30-50%. I calculated the increase of quantity of goods sold that was needed at each of our discount amounts, dependent on the realized profit margin. Using that information, I was able to create an interactive dashboard for an executive user, where they would be able to input the profit margin for each product category and determine whether the change in quantity of goods sold at discount X% was profitable for Northwind.

See an example of the workbook below:

![alt text](https://github.com/zachzazueta/Northwinds_redo/blob/master/tableau.PNG)

The full workbook can be viewed here: https://public.tableau.com/profile/zach.zazueta#!/vizhome/NorthwindsAnalysis/Dashboard1 on Tableau Public.

Improvements to the workbook would include:
- Assuming connection to a live data source for sales information and COGS information, calculated profit margin and delta quantity of goods sold could be integrated and updated on a rolling basis.


Here is a quick look at the difference between average ship time split by Shipper:  
![alt_text](https://github.com/zachzazueta/Northwinds_redo/blob/master/meantts.png)
