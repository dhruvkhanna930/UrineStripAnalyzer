/*
Auto-generated by: https://github.com/pmndrs/gltfjsx
Command: npx gltfjsx@6.2.18 bug.gltf 
Author: vivimayza.vc (https://sketchfab.com/vivimayza.vc)
License: CC-BY-4.0 (http://creativecommons.org/licenses/by/4.0/)
Source: https://sketchfab.com/3d-models/wii-toy-story-3-peas-in-a-pod-c726dc17c7f347e9ab9ade65b01e6f4f
Title: Wii - Toy Story 3 - Peas In A Pod
*/

import React, { useRef } from 'react'
import { useGLTF } from '@react-three/drei'

export default  function Model(props) {
  const { nodes, materials } = useGLTF('/bug.gltf')
  return (
    <group {...props} dispose={null}>
      <group rotation={[-Math.PI / 2, 0, 0]}>
        <group rotation={[Math.PI / 2, 0, 0]}>
          <mesh geometry={nodes.Object_3.geometry} material={materials.peasinapod_d_png} />
          <mesh geometry={nodes.Object_4.geometry} material={materials.peasinapod_d_png} />
        </group>
      </group>
    </group>
  )
}

useGLTF.preload('/bug.gltf')
