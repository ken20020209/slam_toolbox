from launch import LaunchDescription
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch.actions import DeclareLaunchArgument, LogInfo

def generate_launch_description():
    params_file = LaunchConfiguration('params_file', default=get_package_share_directory("slam_toolbox") + '/config/mapper_params_localization.yaml')

    declare_params_file_cmd = DeclareLaunchArgument(
        'params_file',
        default_value=params_file,
        description='Full path to the ROS2 parameters file to use for the slam_toolbox node')

    return LaunchDescription([
        declare_params_file_cmd,
        launch_ros.actions.Node(
          parameters=[
            params_file
          ],
          package='slam_toolbox',
          executable='localization_slam_toolbox_node',
          name='slam_toolbox',
          output='screen'
        )
    ])
