#!/usr/bin/env python

"""Generate video dataset for video stitching"""

import glob
import os
import sys
import time

try:
    sys.path.append(glob.glob('./carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla

import argparse
import logging
from numpy import random

def image_process(image):
    pass

def main():
    argparser = argparse.ArgumentParser(
        description=__doc__)
    argparser.add_argument(
        '-t', '--time',
        metavar='T',
        default=200,
        type=int,
        help='Time of car monitor video generation (default: 200)')
    args = argparser.parse_args()
    try:
        actors = []
        client = carla.Client('localhost',2000)
        client.set_timeout(2.0)
        world = client.get_world()
        blueprint_library = world.get_blueprint_library()

        # spawn car
        vehicle_bp = random.choice(blueprint_library.filter('vehicle.*.*'))
        spawn_points = world.get_map().get_spawn_points()
        point = random.choice(spawn_points)
        my_vehicle = world.spawn_actor(vehicle_bp, point)
        my_vehicle.apply_control(carla.VehicleControl(throttle=1.0, steer=-1.0))
        my_vehicle.set_autopilot(True)
        actors.append(my_vehicle)

        # spawn camera which added to car
        camera_bp = blueprint_library.find('sensor.camera.rgb')

        transform1 = carla.Transform(carla.Location(x=1.5,y=-0.5,z=1.5),carla.Rotation(yaw=-45))
        camera1 = world.spawn_actor(camera_bp, transform1, attach_to=my_vehicle)
        camera1.listen(lambda image: image.save_to_disk('output/c1/%06d.png' % image.frame))

        transform2 = carla.Transform(carla.Location(x=1.5,y=0,z=1.5))
        camera2 = world.spawn_actor(camera_bp, transform2, attach_to=my_vehicle)
        camera2.listen(lambda image: image.save_to_disk('output/c2/%06d.png' % image.frame))

        transform3 = carla.Transform(carla.Location(x=1.5,y=0.5,z=1.5),carla.Rotation(yaw=45))
        camera3 = world.spawn_actor(camera_bp, transform3, attach_to=my_vehicle)
        camera3.listen(lambda image: image.save_to_disk('output/c3/%06d.png' % image.frame))

        actors.append(camera1)
        actors.append(camera2)
        actors.append(camera3)

        time.sleep(args.time)
    finally:
        for actor in actors:
            actor.destroy()

if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        print('\ndone.')
