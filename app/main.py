def get_human_age(cat_age: int, dog_age: int) -> list:
    def calculate_human_age(animal_age, first_years, second_years, subsequent_years):
        if animal_age < first_years:
            return 0
        if animal_age < first_years + second_years:
            return 1
        return 2 + (animal_age - first_years - second_years) // subsequent_years

    cat_human_age = calculate_human_age(cat_age, 15, 9, 4)
    dog_human_age = calculate_human_age(dog_age, 15, 9, 5)

    return [cat_human_age, dog_human_age]
