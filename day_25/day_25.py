def read_input():
    with open("input.txt") as lines:
        return list(int(line) for line in lines.readlines())


class RFIDEncrypter:
    divider = 20201227

    def calculate_loop_size(self, public_key):
        subject_number = 7
        result = 1
        loop_size = 0
        while result != public_key:
            result *= subject_number
            result = result % self.divider
            loop_size += 1
        return loop_size

    def encrypt_key(self, public_key, loop_size):
        result = 1
        for _ in range(loop_size):
            result *= public_key
            result = result % self.divider
        return result


cc_key, door_key = read_input()
rfid_encrypter = RFIDEncrypter()
cc_loop_size = rfid_encrypter.calculate_loop_size(cc_key)
door_loop_size = rfid_encrypter.calculate_loop_size(door_key)
encryption_key = rfid_encrypter.encrypt_key(cc_key, door_loop_size)
print(encryption_key)
