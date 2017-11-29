from unittest import TestCase

from src.com.victuxbb.hanoitowerspuzzle.HanoiTower import HanoiTower


class TestHanoiTower(TestCase):
    def test_start_with_one_disk(self):
        hanoi_instance = HanoiTower(disks=1)
        moves = hanoi_instance.run()
        self.assertEqual(moves, 1)

    def test_start_with_two_disks(self):
        hanoi_instance = HanoiTower(disks=2)
        moves = hanoi_instance.run()
        self.assertEqual(moves, 3)

    def test_start_with_three_disks(self):
        hanoi_instance = HanoiTower(disks=3)
        moves = hanoi_instance.run()
        self.assertEqual(moves, 7)

    def test_start_with_six_disks(self):
        hanoi_instance = HanoiTower(disks=6)
        moves = hanoi_instance.run()
        self.assertEqual(moves, 63)
