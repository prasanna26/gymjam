import pickle
import glob
import os

CHECKPOINT_EXTENSION = "pkl"

class Checkpoint:
    def __init__(self, checkpoint_data=None,
              checkpoint_enabled=None,
              checkpoint_dir=None,
              checkpoint_prefix=None,
              checkpoint_resume=None,
              checkpoint_frequency=None,
              checkpoint_file_name=None,
              search_type=None
        ):
        # Options
        self.checkpoint_data = checkpoint_data
        self.checkpoint_enabled = checkpoint_enabled
        self.checkpoint_dir = checkpoint_dir
        self.checkpoint_prefix = checkpoint_prefix
        self.checkpoint_file_name = checkpoint_file_name
        self.checkpoint_frequency = checkpoint_frequency
        self.checkpoint_resume = checkpoint_resume
        self.search_type = search_type
        self._id = 0
        # Load data from file if a checkpoint filename is provided
        if self.checkpoint_file_name:
            self.checkpoint_data = self.load_checkpoint_from_file(self.checkpoint_file_name)

    def next_id(self):
        self._id += 1
        return self._id

    def load_checkpoint_from_file(self, checkpoint_file_name):
        checkpoint_data = None
        with open(checkpoint_file_name, "rb") as f:
            checkpoint_data = pickle.load(f)
        return checkpoint_data

    def find_latest_checkpoint(self):
        patt = self.glob()
        checkpoints_found = glob.glob(patt)
        # TODO: add file sorting / preference rules?
        checkpoint_data = None
        if checkpoints_found:
            last_checkpoint = checkpoints_found.pop()
            print("Found resumable checkpoint data at: ", last_checkpoint)
            with open(last_checkpoint, "rb") as f:
                checkpoint_data = pickle.load(f)
        return checkpoint_data

    def glob(self):
        return "{}/{}*.{}".format(self.checkpoint_dir, self.checkpoint_prefix, CHECKPOINT_EXTENSION)

    def get_path(self, label=''):
        return os.path.join(self.checkpoint_dir,
                                       "{}_{}.{}".format(self.checkpoint_prefix, label, CHECKPOINT_EXTENSION))

    def save(self, data=None):
        # Update the main checkpoint file. using 'latest' label
        checkpoint_file_name = self.get_path('latest')
        with open(checkpoint_file_name, "wb") as f:
            pickle.dump(data, f)

        # If it's been enough time since the last incremental checkpoint, create one
        next_id = self.next_id()
        if next_id % self.checkpoint_frequency == 0:
            # save a secondary checkpoint
            checkpoint_file_name = self.get_path(label=str(int(next_id / self.checkpoint_frequency)))
            with open(checkpoint_file_name, "wb") as f:
                pickle.dump(data, f)