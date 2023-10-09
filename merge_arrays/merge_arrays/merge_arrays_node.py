import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])

    return result

class MergeArraysNode(Node):

    def __init__(self):
        super().__init__('merge_arrays_node')
        
        # Create subscribers for input arrays
        self.subscription1 = self.create_subscription(
            Int32MultiArray,
            '/input/array1',
            self.array1_callback,
            10
        )
        self.subscription2 = self.create_subscription(
            Int32MultiArray,
            '/input/array2',
            self.array2_callback,
            10
        )
        
        self.array1 = []
        self.array2 = []
        
        # Create publisher for the merged array
        self.publisher = self.create_publisher(Int32MultiArray, '/output/array', 10)

    def array1_callback(self, msg):
        self.array1 = msg.data
        self.merge_and_publish()

    def array2_callback(self, msg):
        self.array2 = msg.data
        self.merge_and_publish()

    def merge_and_publish(self):
        # Only attempt to merge and publish if both arrays are available
        if self.array1 and self.array2:
            # Merge the two sorted arrays using merge sort
            merged_array = merge_sort(self.array1 + self.array2)

            # Publish the merged array
            msg = Int32MultiArray(data=merged_array)
            self.publisher.publish(msg)
            self.get_logger().info('Merged array published: {}'.format(merged_array))

def main(args=None):
    rclpy.init(args=args)
    node = MergeArraysNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

