from launch import LaunchDescription
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch.actions import DeclareLaunchArgument, LogInfo

def generate_launch_description():
    params_file = LaunchConfiguration('params_file', default=get_package_share_directory("slam_toolbox") + '/config/mapper_params_localization.yaml')
    namespace=LaunchConfiguration('namespace',default='RobotDogConnector')
    namespace_declare=DeclareLaunchArgument(
            'namespace',
            default_value=namespace,
            description='Name of the RobotDogConnector node'
        )
    declare_params_file_cmd = DeclareLaunchArgument(
        'params_file',
        default_value=params_file,
        description='Full path to the ROS2 parameters file to use for the slam_toolbox node')
    declare_initial_pose_cmd = DeclareLaunchArgument(
        'initial_pose',
        default_value='[0.0,0.0,0.0]',
        description='Enable initial_pose')
    declare_map_cmd = DeclareLaunchArgument(
        'map',
        default_value='mapa',
        description='Enable map')
    return LaunchDescription([
        declare_params_file_cmd,
        declare_initial_pose_cmd,
        declare_map_cmd,
        namespace_declare,
        launch_ros.actions.Node(
          parameters=[
            params_file,
            {'map_file_name':LaunchConfiguration('map')},
            {'map_start_pose':LaunchConfiguration('initial_pose')},
            {'odom_frame':PythonExpression(["'",namespace,"'+","'/odom'"])},
            {'base_frame':PythonExpression(["'",namespace,"'+","'/base_footprint'"])},
          ],
          package='slam_toolbox',
          executable='localization_slam_toolbox_node',
          name='slam_toolbox',
          output='screen',
          remappings=[('/scan', 'scan')]
        )
    ])
