# Copyright (c) 2018 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Launch realsense2_camera node without rviz2."""
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.substitutions import ThisLaunchFileDir
from launch.launch_description_sources import PythonLaunchDescriptionSource
import sys
import pathlib
sys.path.append(str(pathlib.Path(__file__).parent.absolute()))
import rs_launch

local_parameters = [{'name': 'camera_name1',            'default': 'D435i', 'description': 'camera unique name'},
                    {'name': 'device_type1',            'default': 'd4.', 'description': 'choose device by type'},
                    {'name': 'enable_pointcloud1',      'default': 'true', 'description': 'enable pointcloud'},
                    {'name': 'enable_gyro1',            'default': 'true', 'description': ''},                           
                    {'name': 'enable_accel1',           'default': 'true', 'description': ''}, 
                    {'name': 'depth_fps1',              'default': '6.0', 'description': ''},   
                    {'name': 'color_fps1',              'default': '6.0', 'description': ''},                           
                    {'name': 'gyro_fps1',               'default': '200.0', 'description': ''},                           
                    {'name': 'accel_fps1',              'default': '63.0', 'description': ''},    
                    {'name': 'depth_width1',            'default': '640', 'description': 'depth image width'},                           
                    {'name': 'depth_height1',           'default': '480', 'description': 'depth image height'},                           
                    {'name': 'enable_depth1',           'default': 'true', 'description': 'enable depth stream'},
                    {'name': 'color_width1',            'default': '640', 'description': 'color image width'},                           
                    {'name': 'color_height1',           'default': '480', 'description': 'color image height'},                           
                    {'name': 'enable_color1',           'default': 'true', 'description': 'enable color stream'},
                    {'name': 'enable_sync1',            'default': 'true', 'description': ''},
                    {'name': 'align_depth1',            'default': 'true', 'description': ''},
                    {'name': 'allow_no_texture_points1','default': 'true', 'description': ''},
                    {'name': 'ordered_pc1',             'default': 'true', 'description': ''},
                    {'name': 'camera_name2',            'default': 'T265', 'description': 'camera unique name'},
                    {'name': 'device_type2',            'default': 't265', 'description': 'choose device by type'},
                    {'name': 'fisheye_fps2',            'default': '30.0', 'description': ''},                           
                    {'name': 'enable_fisheye12',        'default': 'false', 'description': 'topic for T265 wheel odometry'},
                    {'name': 'enable_fisheye22',        'default': 'false', 'description': 'topic for T265 wheel odometry'},
                    {'name': 'enable_pose2',            'default': 'true', 'description': 'enable pose stream'},
                    #{'name': 'tf_publish_rate',         'default': '0.0', 'description': 'Rate of publishing static_tf'},
                    #{'name': 'publish_tf',              'default': 'false', 'description': 'Enable/disable publishing static and dynamic TFs'},
                   ]
                   

def generate_launch_description():
    return LaunchDescription(
        rs_launch.declare_configurable_parameters(local_parameters) + 
        [
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([ThisLaunchFileDir(), '/rs_multi_camera_launch.py']),
            launch_arguments=rs_launch.set_configurable_parameters(local_parameters).items(),
        ),
    ])
