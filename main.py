import pandas as pd

def count(column):
    return sum(1 for x in column if not pd.isnull(x))

def mean(colums):
	return (sum(colums)/ count)


def main():
	print("start")
	df = pd.read_csv("./datasets/dataset_train.csv")
	print(df.head())
	stats = {}
	count = len(df['Index'])
	for colums in df.columns:
		print(colums)
		if pd.api.types.is_numeric_dtype(df[colums]):
			means_value = df[colums].sum() /count 
			stats[colums] = {
				'Count' : count,
				'Mean' : means_value,
				'Std': std,
				'Min' : min,
				'25%' : first_quarter,
				'50%' : second_quarter,
				'75%' : third_quarter,
				'Max' : max
			}
			



if __name__ == "__main__":
	main()