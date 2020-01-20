import uuid
import random


def add_uuid(filepath, output_path):
    with open(filepath, 'r') as istr:
        with open(output_path, 'w') as ostr:
            for i, line in enumerate(istr):
                line = line.rstrip('\n') + ',' + str(uuid.uuid4())
                print(line, file=ostr)


def test_unique_uuid(filepath, ofp, n):
    # hashset = set()
    id_list = []
    with open(filepath, 'r') as istr:
        for i, line in enumerate(istr):
            uuid = line.split(',')[-1]
            # if uuid in hashset:
            #     print("duplicate uuid: " + uuid)
            #     break
            # hashset.add(uuid)
            id_list.append(uuid)
    # print(len(hashset))
    n_unique_random_ids = random.sample(range(1, 2000001), n)
    with open(ofp, 'w') as ostr:
        for id in n_unique_random_ids:
            print(id_list[id], file=ostr)


def get_list_from_file(filepath):
    ids = []
    with open(filepath, 'r') as istr:
        for i, line in enumerate(istr):
            ids.append(line.rstrip('\n'))
    return ids


def correct_date_format(filepath, ofp):
    with open(filepath, 'r') as istr:
        with open(ofp, 'w') as ostr:
            for i, line in enumerate(istr):
                line = line.rstrip("\n")
                if i == 0:
                    print(line, file=ostr)
                    continue
                # line = line.rstrip('\n') + ',' + str(uuid.uuid4())
                new_line = ""
                data = line.split(",")
                length = len(data)
                j = 0
                for x in range(length):
                    if j in (4, 24, 44, 64, 84):
                        date = data[x]
                        date_list = date.split("-")
                        date_list[0] = "1971"
                        if len(date_list[1]) < 2:
                            date_list[1] = "0" + date_list[1]
                        if len(date_list[2]) < 2:
                            date_list[2] = "0" + date_list[2]
                        if int(date_list[2]) > 27:
                            date_list[2] = "27"
                        date_formatted = ""
                        for y in date_list:
                            date_formatted += (y + "-")
                        date_formatted = date_formatted.rstrip("-")
                        new_line += (date_formatted + ",")
                    else:
                        new_line += (data[x] + ",")
                    j += 1
                new_line = new_line.rstrip(",")
                print(new_line, file=ostr)


def print_random(filepath):
    n_unique_random_ids = random.sample(range(1, 2000001), 5)
    print(n_unique_random_ids)
    with open(filepath, 'r') as istr:
        for i, line in enumerate(istr):
            if i in n_unique_random_ids:
                print(line)


if __name__ == '__main__':
    # add_uuid("/Users/adheer/Downloads/Prediction100columns_2M_new.csv",
    #          "/Users/adheer/Downloads/Prediction100columns_2M_new_uuid.csv")
    # test_unique_uuid("/Users/adheer/Downloads/Prediction100columns_2M_new_uuid.csv",
    #                  "/Users/adheer/Downloads/ten_k_ids.txt",
    #                  10000)
    # test_unique_uuid("/Users/adheer/Downloads/Prediction100columns_2M_new_uuid.csv",
    #                  "/Users/adheer/Downloads/hundred_k_ids.txt",
    #                  100000)
    # print(get_list_from_file("/Users/adheer/Downloads/hundred_k_ids.txt"))
    # correct_date_format("/Users/adheer/Downloads/Prediction100columns_2M_new_uuid.csv",
    #                     "/Users/adheer/Downloads/Prediction100columns_2M_new_uuid_fixed_date_format.csv")
    # print_random("/Users/adheer/Downloads/Prediction100columns_2M_new_uuid_fixed_date_format.csv")
    # test_unique_uuid("/Users/adheer/Downloads/Prediction100columns_2M_new_uuid.csv",
    #                  "/Users/adheer/Downloads/twenty_k_ids.txt",
    #                  20000)
    # test_unique_uuid("/Users/adheer/Downloads/Prediction100columns_2M_new_uuid.csv",
    #                  "/Users/adheer/Downloads/thirty_k_ids.txt",
    #                  30000)
    # test_unique_uuid("/Users/adheer/Downloads/Prediction100columns_2M_new_uuid.csv",
    #                  "/Users/adheer/Downloads/forty_k_ids.txt",
    #                  40000)
    # test_unique_uuid("/Users/adheer/Downloads/Prediction100columns_2M_new_uuid.csv",
    #                  "/Users/adheer/Downloads/fifty_k_ids.txt",
    #                  50000)
    # test_unique_uuid("/Users/adheer/Downloads/Prediction100columns_2M_new_uuid.csv",
    #                  "/Users/adheer/Downloads/sixty_k_ids.txt",
    #                  60000)
    # test_unique_uuid("/Users/adheer/Downloads/Prediction100columns_2M_new_uuid.csv",
    #                  "/Users/adheer/Downloads/seventy_k_ids.txt",
    #                  70000)
    # test_unique_uuid("/Users/adheer/Downloads/Prediction100columns_2M_new_uuid.csv",
    #                  "/Users/adheer/Downloads/eighty_k_ids.txt",
    #                  80000)
    # test_unique_uuid("/Users/adheer/Downloads/Prediction100columns_2M_new_uuid.csv",
    #                  "/Users/adheer/Downloads/ninety_k_ids.txt",
    #                  90000)
    correct_date_format("/Users/adheer/Downloads/Prediction100columns_2M_new_uuid_fixed_date_format.csv",
                        "/Users/adheer/Downloads/Prediction100columns_2M_new_uuid_fixed_date_format_updated.csv")
