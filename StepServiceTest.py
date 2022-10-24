from Step import Step
from StepProcessor import StepService

import unittest


class StepServieTest(unittest.TestCase):
    step_service = StepService()

    def tearDown(self):
        self.step_service.history = []

    def test_slash_like1(self):
        self.step_service.process_step(Step(1, 1))
        self.step_service.process_step(Step(2, 2))

        self.assertTrue(self.step_service.process_step(Step(3, 3)))

    def test_slash_like2(self):
        self.step_service.process_step(Step(1, 1))
        self.step_service.process_step(Step(5, 5))

        self.assertFalse(self.step_service.process_step(Step(9, 9)))

    def test_column(self):
        self.step_service.process_step(Step(1, 1))
        self.step_service.process_step(Step(1, 2))

        self.assertTrue(self.step_service.process_step(Step(1, 3)))

    def test_row(self):
        self.step_service.process_step(Step(1, 1))
        self.step_service.process_step(Step(2, 1))

        self.assertTrue(self.step_service.process_step(Step(3, 1)))
