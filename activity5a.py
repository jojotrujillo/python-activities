# Activity 5a
import copy


def deduplicator(sports_list):
    i, j, k = 0, 1, 0  # i, j, k are counters

    while i < len(sports_list):
        k = sports_list.count(sports_list[i])  # get number of occurrences for item in list

        if k != 1:  # if there's not just 1 occurrence
            while j < len(sports_list):
                if sports_list[i] == sports_list[j]:
                    sports_list.pop(j)
                    continue

                j += 1

        i += 1
        j = i + 1

    return copy.deepcopy(sports_list)


def main():
    sports = ['rugby', 'archery', 'rugby', 'soccer', 'tennis', 'baseball', 'basketball', 'soccer', 'track',
              'volleyball', 'wrestling', 'swimming', 'racketball', 'basketball', 'hockey',
              'biking', 'handball', 'badminton']

    print('List Deduplicator Function\n\n'
          'Initial List of Sports\n'
          + str(sports))  # cast list to str for print()

    unique_sports = deduplicator(sports)

    unique_sports.sort()

    print('\nList of unique names after running through the deduplicator program\n'
          + str(unique_sports))


# run main()
main()
# Done!
