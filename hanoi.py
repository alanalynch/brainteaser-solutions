#!/usr/bin/python

class Towers():
    def hanoi(self, disk, first, last, temp):

        if disk == 0:
            # base case - disk 0 is the smallest so can move anywhere
            print "move disk 0 from " + first + " to " + last

        else:
            # otherwise move the disk on the source peg to the temp peg
            # which here is "last"
            self.hanoi(disk - 1, first, temp, last)

            print "move disk " + str(disk) + " from " + first + " to " + last

            # then move same disk from temp to last, so what we're actually
            # doing is migrating disks around in between via recursion
            self.hanoi(disk - 1, temp, last, first)


if __name__=='__main__':

    towers = Towers()

    print "3 disk solution:\n"
    towers.hanoi(2,"A","B","C")
    print "\n\n\n"

    print "6 disk solution:\n"
    towers.hanoi(5,"A","B","C")

