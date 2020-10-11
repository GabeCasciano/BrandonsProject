from organization import person

if __name__ == "__main__":
    temp = person("gabe",23,1)
    print(temp.format_csv())