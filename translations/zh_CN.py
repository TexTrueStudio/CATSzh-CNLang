dictionary = {
    # Class.label / Class.desc (tooltip)
    # Class.property

    # Language name
    'name': 'zh_CN',

    # Main file
    'Main.error.restartAdmin': '\n\n发现CATS安装有问题!'
                               '\n要解决这个问题，请以管理员身份重新启动Blender!     '
                               '\n',
    'Main.error.deleteFollowing': '                                                                                                                                                                                    '
                                  '                     '
                                  '\n\n发现CATS安装有问题!'
                                  '\n要解决这个问题，请删除addons文件夹内的以下文件和文件夹:'
                                  '\n',
    'Main.error.installViaPreferences': '\n\n发现CATS安装有问题!'
                                        '\n请通过用户偏好设置安装CATS并重启Blender!'
                                        '\n',
    'Main.error.restartAndEnable': '\n\n发现并修复了CATS安装故障!'
                                   '\n请重新启动Blender并再次启用CATS!'
                                   '\n',
    'Main.error.unsupportedVersion': '\n\nCats不支持2.79以下的Blender版本。 '
                                     '\n请使用Blender 2.79或更高版本。'
                                     '\n',
    'Main.error.beta2.80': '\n\n你还在Blender 2.80的测试版上!'
                           '\n请更新到Blender 2.80的正式版本。'
                           '\n',
    'Main.error.restartAndEnable_alt': '\n\n请重新启动Blender并再次启用CATS!'
                                       '\n',

    # UI Main
    'ToolPanel.label': 'Cats Blender Plugin',
    'ToolPanel.category': 'CATS',

    # UI Armature
    'ArmaturePanel.label': '模型',
    'ArmaturePanel.warn.oldBlender1': '检测到旧版Blender!',
    'ArmaturePanel.warn.oldBlender2': '有些功能可能无法使用',
    'ArmaturePanel.warn.oldBlender3': '请更新到Blender 2.79!',
    'ArmaturePanel.warn.noDict1': '没有找到 Dictionary!',
    'ArmaturePanel.warn.noDict2': '翻译可以用，但没有优化。',
    'ArmaturePanel.warn.noDict3': '重新安装Cats来解决这个问题。',
    'ArmaturePanel.ImportAnyModel.label': '导入模型',
    'ModelSettings.label': '修复模型设置',
    'ModelSettings.warn.fbtFix1': '全身跟踪修复',
    'ModelSettings.warn.fbtFix2': '不再需要VRChat。',
    'ModelSettings.warn.fbtFix3': '它仍然可以在模型选项中使用。',

    # UI Manual
    'ManualPanel.label': '模型选项',
    'ManualPanel.separateBy': '分别为:',
    'ManualPanel.SeparateByMaterials.label': '材料(Materials)',
    'ManualPanel.SeparateByLooseParts.label': '松动部件(Loose Parts)',
    'ManualPanel.SeparateByShapekeys.label': '形状(Shapes)',
    'ManualPanel.joinMeshes': '合并网格:',
    'ManualPanel.JoinMeshes.label': '所有(All)',
    'ManualPanel.JoinMeshesSelected.label': '选定(Selected)',
    'ManualPanel.mergeWeights': '合并权重:',
    'ManualPanel.MergeWeights.label': '父体（To Parents）',
    'ManualPanel.MergeWeightsToActive.label': '激活（To Active）',
    'ManualPanel.translate': '翻译:',
    'ManualPanel.TranslateAllButton.label': '全部(All)',
    'ManualPanel.TranslateShapekeyButton.label': '形状关键点(Shape Keys)',
    'ManualPanel.TranslateObjectsButton.label': '对象(Objects)',
    'ManualPanel.TranslateBonesButton.label': '骨骼(Bones)',
    'ManualPanel.TranslateMaterialsButton.label': '材料(Materials)',
    'ManualPanel.delete': '删除:',
    'ManualPanel.RemoveZeroWeightBones.label': '零权重骨骼(Zero Weight Bones)',
    'ManualPanel.RemoveConstraints': '限制因素',
    'ManualPanel.RemoveZeroWeightGroups': '零权重顶点组(Zero Weight Vertex Groups)',
    'ManualPanel.normals': '规范:',
    'ManualPanel.RecalculateNormals.label': '重新计算',
    'ManualPanel.FlipNormals.label': '翻转',
    'ManualPanel.fbtFix': '全身跟踪修复:',
    'ManualPanel.FixFBTButton.label': '添加(Add)',
    'ManualPanel.RemoveFBTButton.label': '删除(Remove)',

    # UI Custom
    'CustomPanel.label': '自定义模型创建',
    'CustomPanel.mergeArmatures': '合并臂架:',
    'CustomPanel.warn.twoArmatures': '需要两个臂架!',
    'CustomPanel.mergeInto': '基础(Base)',
    'CustomPanel.toMerge': '合并(To Merge)',
    'CustomPanel.attachToBone': '附在(Attach to)',
    'CustomPanel.armaturesCanMerge': '臂架可以自动合并',
    'CustomPanel.attachMesh1': '网格附在臂架上:',
    'CustomPanel.attachMesh2': '网格（Mesh)',
    'CustomPanel.warn.noArmOrMesh1': '需要一个臂架和网格!',
    'CustomPanel.warn.noArmOrMesh2': '确保网格没有父体。',

    # UI Decimation
    'DecimationPanel.label': '抽取',
    'DecimationPanel.decimationMode': '抽取模式:',
    'DecimationPanel.safeModeDesc': ' 不错的结果——无形状节点损失(Decent results - No shape key loss)',
    'DecimationPanel.halfModeDesc': ' 良好的结果-最小形状节点丢失(Good results - Minimal shape key loss)',
    'DecimationPanel.fullModeDesc': ' 一致的结果-全部形状节点丢失（Consistent results - Full shape key loss）',
    'DecimationPanel.smartModeDesc': ' 最佳效果-保留形状键(Best results - Preserve shape keys)',
    'DecimationPanel.customSeparateMaterials': '从按物料分离开始(Start by Separating by Materials):',
    'DecimationPanel.SeparateByMaterials.label': '按材料分开(Separate by Materials)',
    'DecimationPanel.customJoinMeshes': '通过加入网格停止(Stop by Joining Meshes):',
    'DecimationPanel.customWhitelist': '白名单:',
    'DecimationPanel.warn.noShapekeySelected': '未选择形状键(No shape key selected)',
    'DecimationPanel.warn.noDecimation': '每个网格都被选中。这等于无抽取。(Every mesh is selected. This equals no Decimation.)',
    'DecimationPanel.warn.noMeshSelected': '未选择网格',
    'DecimationPanel.warn.emptyList': '两个列表都是空的，等于完全抽取!',
    'DecimationPanel.warn.correctWhitelist': '抽取时考虑两个白名单',
    'DecimationPanel.preset.excellent.label': 'Excellent',
    'DecimationPanel.preset.excellent.description': 'The maximum number of tris you can have for an Excellent rating.',
    'DecimationPanel.preset.good.label': 'Good',
    'DecimationPanel.preset.good.description': 'The maximum number of tris you can have for a Good rating.',
    'DecimationPanel.preset.quest.label': 'Quest',
    'DecimationPanel.preset.quest.description': 'The recommended number of tris for Quest avatars.\n'
                                                'A hard limit will be established in the future that will not be much more than this.',
    'DecimationPanel.warn.notIfBaking': "Not reccomended if baking!",

    # UI Eye tracking
    'EyeTrackingPanel.label': 'Eye Tracking',
    'EyeTrackingPanel.error.noMesh': 'No meshes found!',
    'EyeTrackingPanel.error.noArm': 'No model found!',
    'EyeTrackingPanel.error.wrongNameArm1': 'Your armature has to be named \'Armature\'',
    'EyeTrackingPanel.error.wrongNameArm2': '      for Eye Tracking to work!',
    'EyeTrackingPanel.error.wrongNameArm3': '      (currently \'',
    'EyeTrackingPanel.error.wrongNameBody1': 'The mesh containing the eyes has to be',
    'EyeTrackingPanel.error.wrongNameBody2': '      named \'Body\' for Eye Tracking to work!',
    'EyeTrackingPanel.error.wrongNameBody3': '      (currently \'',
    'EyeTrackingPanel.warn.assignEyes1': 'Don\'t forget to assign \'LeftEye\' and \'RightEye\'',
    'EyeTrackingPanel.warn.assignEyes2': '      to the eyes in Unity!',

    # UI Visemes
    'VisemePanel.label': 'Visemes',
    'VisemePanel.error.noMesh': 'No meshes found!',

    # UI Bone_root
    'BoneRootPanel.label': 'Bone Parenting',

    # UI Optimization
    'OptimizePanel.label': 'Optimization',
    'OptimizePanel.atlasDesc': 'A greatly improved Atlas Generator.',
    'OptimizePanel.atlasAuthor': 'Made by Shotariya',
    'OptimizePanel.matCombDisabled1': 'Material Combiner is not enabled!',
    'OptimizePanel.matCombDisabled2': 'Enable it in your user preferences:',
    'OptimizePanel.matCombOutdated1': 'Your Material Combiner is outdated!',
    'OptimizePanel.matCombOutdated2': 'Please update to the latest version.',
    'OptimizePanel.matCombOutdated3': 'Update via the \'Updates\' panel',
    'OptimizePanel.matCombOutdated4': 'in the \'MatCombiner\' tab to the {location}',
    'OptimizePanel.matCombOutdated5_2.79': 'left.',
    'OptimizePanel.matCombOutdated5_2.8': 'right.',
    'OptimizePanel.matCombOutdated6': 'Or download and install it manually:',
    'OptimizePanel.matCombOutdated6_alt': 'Download and install it manually:',
    'OptimizePanel.matCombNotInstalled': 'Material Combiner is not installed!',

    # UI Copy protection
    'CopyProtectionPanel.label': 'Copy Protection',
    'CopyProtectionPanel.desc1': 'Tries to protect your avatar from Unity cache ripping.',
    'CopyProtectionPanel.desc2': 'This protection is not 100% safe!',
    'CopyProtectionPanel.desc3': 'Before use: Read the documentation!',

    # UI Bake
    'BakePanel.label': 'Bake',
    'BakePanel.versionTooOld': 'Only for Blender 2.80+',
    'BakePanel.autodetectlabel': 'Autodetect:',
    'BakePanel.generaloptionslabel': "General options:",
    'BakePanel.noheadfound': "No \"Head\" bone found!",
    'BakePanel.overlapfixlabel': "Overlap fix:",
    'BakePanel.bakepasseslabel': "Bake passes:",
    'BakePanel.alphalabel': "Alpha:",
    'BakePanel.transparencywarning': "Transparency isn't currently selected!",
    'BakePanel.smoothnesswarning': "Smoothness isn't currently selected!",
    'BakePanel.doublepackwarning': "Smoothness packed in two places!",

    # UI Settings & Updates
    'UpdaterPanel.label': 'Settings & Updates',
    'UpdaterPanel.name': 'Settings:',
    'UpdaterPanel.requireRestart1': 'Restart required.',
    'UpdaterPanel.requireRestart2': 'Some changes require a Blender restart.',

    # UI Supporter
    'SupporterPanel.label': 'Supporters',
    'SupporterPanel.desc': 'Do you like this plugin and want to support us?',
    'SupporterPanel.thanks': 'Thanks to our awesome supporters! <3',
    'SupporterPanel.missingName1': 'Is your name missing?',
    'SupporterPanel.missingName2': '     Please contact us in our discord!',

    # UI Credits
    'CreditsPanel.label': 'Credits',
    'CreditsPanel.desc1': 'Cats Blender Plugin (',
    'CreditsPanel.desc2': 'Created by Hotox and GiveMeAllYourCats',
    'CreditsPanel.desc3': 'For the awesome VRChat community <3',
    'CreditsPanel.desc4': 'Special thanks to:',
    'CreditsPanel.descContributors': 'Feilen, Jordo, Ruubick, Shotariya and Neitri',
    'CreditsPanel.desc5': 'Do you need help or found a bug?',

    # Tools Armature
    'FixArmature.label': 'Fix Model',
    'FixArmature.desc': 'Automatically:\n'
                        '- Reparents bones\n'
                        '- Removes unnecessary bones, objects, groups & constraints\n'
                        '- Translates and renames bones & objects\n'
                        '- Merges weight paints\n'
                        '- Corrects the hips\n'
                        '- Joins meshes\n'
                        '- Converts morphs into shapes\n'
                        '- Corrects shading',
    'FixArmature.error.noMesh': ['No mesh inside the armature found!',
                                 'If there are meshes outside of the armature,',
                                 'set the armature as the parent of the meshes.'],
    # Format strings? vvvv t(str, fixed_uv_coords) -> The model was successfully fixed, but there were {} faulty UV
    'FixArmature.error.faultyUV1': 'The model was successfully fixed, but there were {uvcoord} faulty UV coordinates.',
    # 'The model was successfully fixed, but there were ' + str(fixed_uv_coords) + ' faulty UV coordinates.',
    'FixArmature.error.faultyUV2': 'This could result in broken textures and you might have to fix them manually.',
    'FixArmature.error.faultyUV3': 'This issue is often caused by edits in PMX editor.',
    'FixArmature.fixedSuccess': 'Model successfully fixed.',
    'FixArmature.bonesNotFound': 'The following bones were not found:',
    'FixArmature.cantFix1': 'Looks like you found a model which Cats could not fix!',
    'FixArmature.cantFix2': 'If this is a non modified model we would love to make it compatible.',
    'FixArmature.cantFix3': 'Report it to us in the forum or in our discord, links can be found in the Credits panel.',
    'FixArmature.notParent': ' is not parented at all, this will cause problems!',
    'FixArmature.notParentTo1': ' is not parented to ',
    'FixArmature.notParentTo2': ', this will cause problems!',

    # Tools Armature Manual
    'StartPoseMode.label': 'Start Pose Mode',
    'StartPoseMode.desc': 'Starts the pose mode.\n'
                          'This lets you test how your model will move',
    'StartPoseModeNoReset.desc': 'Starts the pose mode without resetting the pose.\n'
                                 'This lets you test how your model will move',

    'StopPoseMode.label': 'Stop Pose Mode',
    'StopPoseMode.desc': 'Stops the pose mode and resets the pose to normal',
    'StopPoseModeNoReset.desc': 'Stops the pose mode and keeps the current pose',

    'PoseToShape.label': 'Pose to Shape Key',
    'PoseToShape.desc': 'This saves your current pose as a new shape key.'
                        '\nThe new shape key will be at the bottom of your shape key list of the mesh',

    'PoseNamePopup.label': 'Give this shapekey a name:',
    'PoseNamePopup.desc': 'Sets the shapekey name. Press anywhere outside to skip',
    'PoseNamePopup.success': 'Pose successfully saved as shape key.',

    'PoseToRest.label': 'Apply as Rest Pose',
    'PoseToRest.desc': 'This applies the current pose position as the new rest position.'
                       '\n'
                       '\nIf you scale the bones equally on each axis the shape keys will be scaled correctly as well!'
                       '\nWARNING: This can have unwanted effects on shape keys, so be careful when modifying the head with this',
    'PoseToRest.success': 'Pose successfully applied as rest pose.',

    'JoinMeshes.label': 'Join Meshes',
    'JoinMeshes.desc': 'Joins all meshes of this model together.'
                       '\nIt also:'
                       '\n  - Reorders all shape keys correctly'
                       '\n  - Applies all transforms'
                       '\n  - Repairs broken armature modifiers'
                       '\n  - Applies all decimation and mirror modifiers'
                       '\n  - Merges UV maps correctly',
    'JoinMeshes.failure': 'Meshes could not be joined!',
    'JoinMeshes.success': 'Meshes joined.',

    'JoinMeshesSelected.label': 'Join Selected Meshes',
    'JoinMeshesSelected.desc': 'Joins all selected meshes of this model together.'
                               '\nIt also:'
                               '\n  - Reorders all shape keys correctly'
                               '\n  - Applies all transforms'
                               '\n  - Repairs broken armature modifiers'
                               '\n  - Applies all decimation and mirror modifiers'
                               '\n  - Merges UV maps correctly',
    'JoinMeshesSelected.error.noSelect': 'No meshes selected! Please select the meshes you want to join in the hierarchy!',
    'JoinMeshesSelected.error.cantJoin': 'Selected meshes could not be joined!',
    'JoinMeshesSelected.success': 'Selected meshes joined.',

    'SeparateByMaterials.label': 'Separate by Materials',
    'SeparateByMaterials.desc': 'Separates selected mesh by materials.\n'
                                '\n'
                                'Warning: Never decimate something where you might need the shape keys later (face, mouth, eyes..)',
    'SeparateByMaterials.success': 'Successfully separated by materials.',

    'SeparateByLooseParts.label': 'Separate by Loose Parts',
    'SeparateByLooseParts.desc': 'Separates selected mesh by loose parts.\n'
                                 'This acts like separating by materials but creates more meshes for more precision',
    'SeparateByLooseParts.success': 'Successfully separated by loose parts.',

    'SeparateByShapekeys.label': 'Separate by Shape Keys',
    'SeparateByShapekeys.desc': 'Separates selected mesh into two parts,'
                                '\ndepending on whether it is effected by a shape key or not.'
                                '\n'
                                '\nVery useful for manual decimation',
    'SeparateByShapekeys.success': 'Successfully separated by shape keys.',

    'SeparateByCopyProtection.label': 'Separate by Copy Protection',
    'SeparateByCopyProtection.desc': 'Separates selected mesh into two parts,'
                                     '\ndepending on whether it is effected by the Cats Copy Protection or not.'
                                     '\n'
                                     '\nUseful if you have the Copy Protection enabled on multiple selected parts of your model',
    'SeparateByCopyProtection.success': 'Successfully separated by shape keys.',

    'SeparateByX.error.noMesh': 'No meshes found!',
    'SeparateByX.error.multipleMesh': 'Multiple meshes found!'
                                      '\nPlease select the mesh you want to separate!',
    'SeparateByX.warn.noSeparation': 'No meshes had to be separated!',

    'MergeWeights.label': 'Merge Weights to Parent',
    'MergeWeights.desc': 'Deletes the selected bones and adds their weight to their respective parents.'
                         '\n'
                         '\nOnly available in Edit or Pose Mode with bones selected',
    'MergeWeights.success': 'Deleted {number} bones and added their weights to their parents.',

    'MergeWeightsToActive.label': 'Merge Weights to Active',
    'MergeWeightsToActive.desc': 'Deletes the selected bones except the active one and adds their weights to the active bone.'
                                 '\nThe active bone is the one you selected last.'
                                 '\n'
                                 '\nOnly available in Edit or Pose Mode with bones selected',
    'MergeWeightsToActive.success': 'Deleted {number} bones and added their weights to the active bone.',

    'ApplyTransformations.label': 'Apply Transformations',
    'ApplyTransformations.desc': 'Applies the position, rotation and scale to the armature and it\'s meshes',
    'ApplyTransformations.success': 'Transformations applied.',

    'ApplyAllTransformations.label': 'Apply All Transformations',
    'ApplyAllTransformations.desc': 'Applies the position, rotation and scale of all objects',
    'ApplyAllTransformations.success': 'Transformations applied.',

    'RemoveZeroWeightBones.label': 'Remove Zero Weight Bones',
    'RemoveZeroWeightBones.desc': 'Cleans up the bones hierarchy, deleting all bones that don\'t directly affect any vertices\n'
                                  'Don\'t use this if you plan to use \'Fix Model\'',
    'RemoveZeroWeightBones.success': 'Deleted {number} zero weight bones.',

    'RemoveZeroWeightGroups.label': 'Remove Zero Weight Vertex Groups',
    'RemoveZeroWeightGroups.desc': 'Cleans up the vertex groups of all meshes, deleting all groups that don\'t directly affect any vertices',
    'RemoveZeroWeightGroups.success': 'Removed {number} zero weight vertex groups.',

    'RemoveConstraints.label': 'Remove Bone Constraints',
    'RemoveConstraints.desc': 'Removes constrains between bones causing specific bone movement as these are not used by VRChat',
    'RemoveConstraints.success': 'Removed all bone constraints.',

    'RecalculateNormals.label': 'Recalculate Normals',
    'RecalculateNormals.desc': 'Makes normals point inside of the selected mesh.\n\n'
                               'Don\'t use this on good looking meshes as this can screw them up.\n'
                               'Use this if there are random inverted or darker faces on the mesh',
    'RecalculateNormals.success': 'Recalculated all normals.',

    'FlipNormals.label': 'Flip Normals',
    'FlipNormals.desc': 'Flips the direction of the faces\' normals of the selected mesh.\n'
                        'Use this if all normals are inverted',
    'FlipNormals.success': 'Flipped all normals.',

    'RemoveDoubles.label': 'Remove Doubles',
    'RemoveDoubles.desc': 'Merges duplicated faces and vertices of the selected meshes.'
                          '\nThis is more safe than doing it manually:'
                          '\n  - leaves shape keys completely untouched'
                          '\n  - but removes less doubles overall',
    'RemoveDoubles.success': 'Removed {number} vertices.',

    'RemoveDoublesNormal.label': 'Remove Doubles Normally',
    'RemoveDoublesNormal.desc': 'Merges duplicated faces and vertices of the selected meshes.'
                                '\nThis is exactly like doing it manually',
    'RemoveDoublesNormal.success': 'Removed {number} vertices.',

    'FixVRMShapesButton.label': 'Fix Koikatsu Shapekeys',
    'FixVRMShapesButton.desc': 'Fixes the shapekeys of Koikatsu models',
    'FixVRMShapesButton.warn.notDetected': 'No shapekeys detected!',
    'FixVRMShapesButton.success': 'Fixed VRM shapekeys.',

    'FixFBTButton.label': 'Fix Full Body Tracking',
    'FixFBTButton.desc': 'WARNING: This fix is no longer needed for VRChat, you should not use it!'
                         '\n'
                         '\nApplies a general fix for Full Body Tracking.'
                         '\nIgnore the \"Spine length zero\" warning in Unity',
    'FixFBTButton.error.bonesNotFound': 'Required bones could not be found!'
                                        '\nPlease make sure that your armature contains the following bones:'
                                        '\n - Hips, Spine, Left leg, Right leg'
                                        '\nExact names are required!',
    'FixFBTButton.error.alreadyApplied': 'Full Body Tracking Fix already applied!',
    'FixFBTButton.success': 'Successfully applied the Full Body Tracking fix.',

    'RemoveFBTButton.label': 'Remove Full Body Tracking Fix',
    'RemoveFBTButton.desc': 'Removes the fix for Full Body Tracking, since it is no longer advised to use it.'
                            '\n'
                            '\nRequires bones:'
                            '\n - Hips, Spine, Left leg, Right leg, Left leg 2, Right leg 2',
    'RemoveFBTButton.error.bonesNotFound': 'Required bones could not be found!'
                                           '\nPlease make sure that your armature contains the following bones:'
                                           '\n - Hips, Spine, Left leg, Right leg, Left leg 2, Right leg 2'
                                           '\nExact names are required!',
    'RemoveFBTButton.error.notApplied': 'The Full Body Tracking Fix is not applied!',
    'RemoveFBTButton.success': 'Successfully removed the Full Body Tracking fix.',

    'DuplicateBonesButton.label': 'Duplicate Bones',
    'DuplicateBonesButton.desc': 'Duplicates the selected bones including their weight and renames them to _L and _R',
    'DuplicateBonesButton.success': 'Successfully duplicated {number} bones.',

    # Tools Armature Custom
    'MergeArmature.label': 'Merge Armatures',
    'MergeArmature.desc': 'Merges the selected merge armature into the base armature.'
                          '\nYou should fix both armatures with Cats first.'
                          '\nOnly move the mesh of the merge armature to the desired position, the bones will be moved automatically',
    'MergeArmature.error.notFound': 'The armature "{name}" could not be found.',
    'MergeArmature.error.checkTransforms': ['Please make sure that the parent of the merge armature has the following transforms:',
                                            ' - Location at 0',
                                            ' - Rotation at 0',
                                            ' - Scale at 1'],
    'MergeArmature.error.pleaseFix': ['Please use the "Fix Model" feature on the selected armatures first!',
                                      'Make sure to select the armature you want to fix above the "Fix Model" button!',
                                      'After that please only move the mesh (not the armature!) to the desired position.'],
    'MergeArmature.success': 'Armatures successfully joined.',

    'AttachMesh.label': 'Attach Mesh',
    'AttachMesh.desc': 'Attaches the selected mesh to the selected bone of the selected armature.'
                       '\n'
                       '\nINFO: The mesh will only be assigned to the selected bone.'
                       '\nE.g.: A jacket won\'t work, because it requires multiple bones',
    'AttachMesh.success': 'Mesh successfully attached to armature.',

    'CustomModelTutorialButton.label': 'How to use',
    'CustomModelTutorialButton.URL': 'https://github.com/michaeldegroot/cats-blender-plugin#custom-model-creation',  # BOOM, now we can point at the Japanese link now ;)
    'CustomModelTutorialButton.success': 'Documentation opened.',

    'merge_armatures.error.transformReset': ['If you want to rotate the new part, only modify the mesh instead of the armature,',
                                             'or select "Apply Transforms"!',
                                             '',
                                             'The transforms of the merge armature got reset and the mesh you have to modify got selected.',
                                             'Now place this selected mesh where and how you want it to be and then merge the armatures again.',
                                             'If you don\'t want that, undo this operation.'],
    'merge_armatures.error.pleaseUndo': ['Something went wrong! Please undo, check your selections and try again.'],

    # Tools Atlas
    'EnableSMC.label': 'Enable Material Combiner',
    'EnableSMC.desc': 'Enables Material Combiner',
    'EnableSMC.success': 'Enabled Material Combiner!',

    'AtlasHelpButton.label': 'Generate Material List',
    'AtlasHelpButton.desc': 'Open useful Atlas Tips',
    'AtlasHelpButton.URL': 'https://github.com/michaeldegroot/cats-blender-plugin/#texture-atlas',
    'AtlasHelpButton.success': 'Atlas Help opened.',

    'InstallShotariya.label': 'Error while loading Material Combiner:',
    'InstallShotariya.error.install1': 'Material Combiner is not installed!',
    'InstallShotariya.error.install2': 'The plugin \'Material Combiner\' by Shotariya is required for this function.',
    'InstallShotariya.error.install3': 'Please download and install it manually:',
    'InstallShotariya.error.enable1': 'Material Combiner is not enabled!',
    'InstallShotariya.error.enable2': 'The plugin \'Material Combiner\' by Shotariya is required for this function.',
    'InstallShotariya.error.enable3': 'Please enable it in your User Preferences.',
    'InstallShotariya.error.version1': 'Material Combiner is outdated!',
    'InstallShotariya.error.version2': 'The latest version is required for this function.',
    'InstallShotariya.error.version3': 'Please download and install it manually:',

    'ShotariyaButton.label': 'Download Material Combiner',
    'ShotariyaButton.URL': 'https://vrcat.club/threads/material-combiner-blender-addon-1-1-3.2255/',
    'ShotariyaButton.success': 'Material Combiner link opened',

    # Tools Bonemerge
    'BoneMergeButton.label': 'Merge Bones',
    'BoneMergeButton.desc': 'Merges the given percentage of bones together.\n'
                            'This is useful to reduce the amount of bones used by Dynamic Bones.',
    'BoneMergeButton.success': 'Merged bones.',

    # Tools Common
    'ShowError.label': 'Report: Error',

    # Tools Copy protection
    'CopyProtectionEnable.label': 'Enable Protection',
    'CopyProtectionEnable.desc': 'Protects your model from piracy. NOT a 100% safe protection!'
                                 '\nRead the documentation before use',
    'CopyProtectionEnable.success': 'Model secured!',

    'CopyProtectionDisable.label': 'Disable Protection',
    'CopyProtectionDisable.desc': 'Removes the copy protections from this model.',
    'CopyProtectionDisable.success': 'Model un-secured!',

    'ProtectionTutorialButton.label': 'Go to Documentation',
    'ProtectionTutorialButton.URL': 'https://github.com/michaeldegroot/cats-blender-plugin#copy-protection',
    'ProtectionTutorialButton.success': 'Documentation',

    # Tools Credits
    'ForumButton.label': 'Go to the Forums',
    'ForumButton.URL': 'https://vrcat.club/threads/cats-blender-plugin.6/',
    'ForumButton.success': 'Forum opened.',

    'DiscordButton.label': 'Join our Discord',
    'DiscordButton.URL': 'https://discord.gg/f8yZGnv',
    'DiscordButton.success': 'Discord opened.',

    'PatchnotesButton.label': 'Latest Patchnotes',
    'PatchnotesButton.URL': 'https://github.com/michaeldegroot/cats-blender-plugin/releases',
    'PatchnotesButton.success': 'Patchnotes opened.',

    # Tools Decimation
    'ScanButton.label': 'Scan for decimation models',
    'ScanButton.desc': 'Separates the mesh.',

    'AddShapeButton.label': 'Add',
    'AddShapeButton.desc': 'Adds the selected shape key to the whitelist.\n'
                           'This means that every mesh containing that shape key will be not decimated.',

    'AddMeshButton.label': 'Add',
    'AddMeshButton.desc': 'Adds the selected mesh to the whitelist.\n'
                          'This means that this mesh will be not decimated.',

    'RemoveShapeButton.label': '',
    'RemoveShapeButton.desc': 'Removes the selected shape key from the whitelist.\n'
                              'This means that this shape key is no longer decimation safe!',

    'RemoveMeshButton.label': '',
    'RemoveMeshButton.desc': 'Removes the selected mesh from the whitelist.\n'
                             'This means that this mesh will be decimated.',

    'AutoDecimateButton.label': 'Quick Decimation',
    'AutoDecimateButton.desc': 'This will automatically decimate your model while preserving the shape keys.\n'
                               'You should manually remove unimportant meshes first.',
    'AutoDecimateButton.error.noMesh': 'No meshes found!',

    'decimate.cantDecimateWithSettings': 'This model can not be decimated to {number} tris with the specified settings.',
    'decimate.safeTryOptions': 'Try to use Custom, Half or Full Decimation.',
    'decimate.halfTryOptions': 'Try to use Custom or Full Decimation.',
    'decimate.customTryOptions': 'Select fewer shape keys and/or meshes or use Full Decimation.',
    'decimate.disableFingersOrIncrease': 'Disable \'Save Fingers\' or increase the Tris Count.',
    'decimate.disableFingers': 'or disable \'Save Fingers\'.',  # This comes after one of the previous xTryOptions
    'decimate.noDecimationNeeded': 'The model already has less than {number} tris. Nothing had to be decimated.',
    'decimate.cantDecimate1': 'The model could not be decimated to {number} tris.',
    'decimate.cantDecimate2': 'It got decimated as much as possible within the limits.',

    # Tools Eyetracking
    'CreateEyesButton.label': 'Create Eye Tracking',
    'CreateEyesButton.desc': 'This will let you track someone when they come close to you and it enables blinking.\n'
                             'You should do decimation before this operation.\n'
                             'Test the resulting eye movement in the \'Testing\' tab.',
    'CreateEyesButton.error.noShapeSelected': 'You have no shape keys selected.'
                                              '\nPlease choose a mesh containing shape keys or check "Disable Eye Blinking".',
    'CreateEyesButton.error.missingBone': 'The bone "{bone}" does not exist.',
    'CreateEyesButton.error.noVertex': 'The bone "{bone}" has no existing vertex group or no vertices assigned to it.'
                                       '\nThis might be because you selected the wrong mesh or the wrong bone.'
                                       '\nAlso make sure that the selected eye bones actually move the eyes in pose mode.',
    'CreateEyesButton.error.dontUse': 'Please do not use "{eyeName}" as the input bone.'
                                      '\nIf you are sure that you want to use that bone please rename it to "{eyeNameShort}".',
    'CreateEyesButton.error.hierarchy': 'Eye tracking will not work unless the bone hierarchy is exactly as following: Hips > Spine > Chest > Neck > Head'
                                        '\nFurthermore the mesh containing the eyes has to be called "Body" and the armature "Armature".',
    'CreateEyesButton.success': 'Created eye tracking!',

    'StartTestingButton.label': 'Start Eye Testing',
    'StartTestingButton.desc': 'This will let you test how the eye movement will look ingame.\n'
                               'Don\'t forget to stop the Testing process afterwards.\n'
                               'Bones "LeftEye" and "RightEye" are required.',

    'StopTestingButton.label': 'Stop Eye Testing',
    'StopTestingButton.desc': 'Stops the testing process.',
    'StopTestingButton.error.tryAgain': 'Something went wrong. Please try eye testing again.',

    'ResetRotationButton.label': 'Reset Rotation',
    'ResetRotationButton.desc': 'This resets the eye positions.',

    'AdjustEyesButton.label': 'Set Range',
    'AdjustEyesButton.desc': 'Lets you re-adjust the movement range of the eyes.\n'
                             'This gets saved',
    'AdjustEyesButton.error.noVertex': 'The bone "{bone}" has no existing vertex group or no vertices assigned to it.'
                                       '\nThis might be because you selected the wrong mesh or the wrong bone.'
                                       '\nAlso make sure to join your meshes before creating eye tracking and make sure that the eye bones actually move the eyes in pose mode.',

    'StartIrisHeightButton.label': 'Start Iris Height Adjustment',
    'StartIrisHeightButton.desc': 'Lets you readjust the distance of the iris from the eye ball.\n'
                                  'Use this to fix clipping of the iris into the eye ball.\n'
                                  'This gets saved.',

    'TestBlinking.label': 'Test',
    'TestBlinking.desc': 'This lets you see how eye blinking will look in-game.',

    'TestLowerlid.label': 'Test',
    'TestLowerlid.desc': 'This lets you see how lowerlids will look in-game.',

    'ResetBlinkTest.label': 'Reset Shapes',
    'ResetBlinkTest.desc': 'This resets the blink testing.',

    # Tools Importer
    'ImportAnyModel.label': 'Import Any Model',
    'ImportAnyModel.desc2.79': 'Import a model of any supported type.'
                               '\n'
                               '\nSupported types:'
                               '\n- MMD: .pmx/.pmd'
                               '\n- XNALara: .xps/.mesh/.ascii'
                               '\n- Source: .smd/.qc'
                               '\n- VRM: .vrm'
                               '\n- FBX .fbx '
                               '\n- DAE: .dae '
                               '\n- ZIP: .zip',
    'ImportAnyModel.desc2.8': 'Import a model of any supported type.'
                              '\n'
                              '\nSupported types:'
                              '\n- MMD: .pmx/.pmd'
                              '\n- XNALara: .xps/.mesh/.ascii'
                              '\n- Source: .smd/.qc/.vta/.dmx'
                              '\n- VRM: .vrm'
                              '\n- FBX: .fbx'
                              '\n- DAE: .dae '
                              '\n- ZIP: .zip',
    'ImportAnyModel.importantInfo.label': 'IMPORTANT INFO (hover here)',
    'ImportAnyModel.importantInfo.desc': 'If you want to modify the import settings, use the button next to the Import button.\n\n',
    'ImportAnyModel.error.emptyZip': 'The selected zip file contains no importable models.',
    'ImportAnyModel.error.unsupportedFBX': 'The FBX file version is unsupported!'
                                           '\nPlease use a tool such as the "Autodesk FBX Converter" to make it compatible.',

    'ZipPopup.label': 'Zip Model Selection:',
    'ZipPopup.desc': 'Shows the models contained in the zip files',
    'ZipPopup.selectModel1': 'Select which model you want to import',
    'ZipPopup.selectModel2': 'Then confirm with OK',

    'get_zip_content.choose': 'Import model "{model}" from the zip "{zipName}?"',

    'ModelsPopup.label': 'Select which you want to import:',
    'ModelsPopup.desc': 'Show individual import options',

    'ImportMMD.label': 'MMD',
    'ImportMMD.desc': 'Import a MMD model (.pmx/pmd)',

    'ImportXPS.label': 'XNALara',
    'ImportXPS.desc': 'Import a XNALara model (.xps/.mesh/.ascii)',

    'ImportSource.label': 'Source',
    'ImportSource.desc': 'Import a Source model (.smd/.qc/.vta/.dmx)',

    'ImportFBX.label': 'FBX',
    'ImportFBX.desc': 'Import a FBX model (.fbx)',

    'ImportVRM.label': 'VRM',
    'ImportVRM.desc': 'Import a VRM model (.vrm)',

    'InstallXPS.label': 'XPS Tools is not installed or enabled!',

    'InstallSource.label': 'Source Tools is not installed or enabled!',

    'InstallVRM.label': 'VRM Importer is not installed or enabled!',

    'InstallX.pleaseInstall1': 'If it is not enabled please enable it in your User Preferences.',
    'InstallX.pleaseInstall2': 'If it is not installed please download and install it manually.',
    'InstallX.pleaseInstall3': 'Make sure to install the version for Blender {blenderVersion}',
    'InstallX.pleaseInstallTesting': 'Currently you have to select \'Testing\' in the addons settings.',

    'EnableMMD.label': 'Mmd_tools is not enabled!',
    'EnableMMD.required1': 'The plugin "mmd_tools" is required for this function.',
    'EnableMMD.required2': 'Please restart Blender.',

    'XpsToolsButton.label': 'Download XPS Tools',
    'XpsToolsButton.URL': 'https://github.com/johnzero7/XNALaraMesh',
    'XpsToolsButton.success': 'XPS Tools link opened',

    'SourceToolsButton.label': 'Download Source Tools',
    'SourceToolsButton.URL': 'https://github.com/Artfunkel/BlenderSourceTools',
    'SourceToolsButton.success': 'Source Tools link opened',

    'VrmToolsButton.label': 'Download VRM Importer',
    'VrmToolsButton.URL_2.79': 'https://github.com/iCyP/VRM_IMPORTER_for_Blender2_79',
    'VrmToolsButton.URL_2.8': 'https://github.com/saturday06/VRM_IMPORTER_for_Blender2_8',
    'VrmToolsButton.success': 'VRM Importer link opened',

    'ExportModel.label': 'Export Model',
    'ExportModel.desc': 'Export this model as .fbx for Unity.\n'
                        '\n'
                        'Automatically sets the optimal export settings',
    'ExportModel.error.notEnabled': 'FBX Exporter not enabled! Please enable it in your User Preferences.',

    'ErrorDisplay.label': 'Warning:',
    'ErrorDisplay.polygons1': 'Too many polygons!',
    'ErrorDisplay.polygons2': 'You have {number} tris in this model, but you shouldn\'t have more than 70,000!',
    'ErrorDisplay.polygons3': 'You should decimate before you export this model.',
    'ErrorDisplay.materials1': 'Model not optimized!',
    'ErrorDisplay.materials2': 'This model has {number} materials!',
    'ErrorDisplay.materials3': 'You should try to have a maximum of 4 materials on your model.',
    'ErrorDisplay.materials4': 'Creating a texture atlas in CATS is very easy, so please make use of it.',
    'ErrorDisplay.meshes1': 'Meshes not joined!',
    'ErrorDisplay.meshes2': 'This model has {number} meshes!',
    'ErrorDisplay.meshes3': 'It is not very optimized and might cause lag for you and others!',
    'ErrorDisplay.meshes3_alt': "It is extremely unoptimized and will cause laugh for you and others!",
    'ErrorDisplay.meshes4': 'You should always join your meshes, it\'s very easy:',
    'ErrorDisplay.JoinMeshes.label': 'Join Meshes',
    'ErrorDisplay.brokenShapekeys1': 'Broken shapekeys!',
    'ErrorDisplay.brokenShapekeys2': 'This model has {number} broken shapekey(s):',
    'ErrorDisplay.brokenShapekeys3': 'You will not be able to upload this model until you fix these shapekeys.',
    'ErrorDisplay.brokenShapekeys4': 'Either delete or repair them before export.',
    'ErrorDisplay.textures1': 'No textures found!',
    'ErrorDisplay.textures2': 'This model has no textures assigned but you have \'Embed Textures\' enabled.',
    'ErrorDisplay.textures3': 'Therefore, no textures will be embedded into the FBX.',
    'ErrorDisplay.textures4': 'This is not an issue, but you will have to import the textures manually into Unity.',
    'ErrorDisplay.eyes1': 'Eyes not named \'Body\'!',
    'ErrorDisplay.eyes2': 'The mesh \'{name}\' has Eye Tracking shapekeys but is not named \'Body\'.',
    'ErrorDisplay.eyes2_alt': 'Multiple meshes have Eye Tracking shapekeys but are not named \'Body\'.',
    'ErrorDisplay.eyes3': 'If you want Eye Tracking to work, rename this mesh to \'Body\'.',
    'ErrorDisplay.eyes3_alt': 'Make sure that the mesh containing the eyes is named \'Body\' in order',
    'ErrorDisplay.eyes4_alt': 'to get Eye Tracking to work.',
    'ErrorDisplay.continue': 'Continue to Export',

    # Tools Material
    'OneTexPerMatButton.label': 'One Material Texture',
    'OneTexPerMatButton.desc': 'Have all material slots ignore extra texture slots as these are not used by VRChat.',

    'OneTexPerMatOnlyButton.label': 'One Material Texture',
    'OneTexPerMatOnlyButton.desc': 'Have all material slots ignore extra texture slots as these are not used by VRChat.'
                                   '\nAlso removes the textures from the material instead of disabling it.'
                                   '\nThis makes no difference, but cleans the list for the perfectionists',

    'ToolsMaterial.error.notCompatible': 'This function is not yet compatible with Blender 2.8!',
    'OneTexPerXButton.success': 'All materials have one texture now.',

    'StandardizeTextures.label': 'Standardize Textures',
    'StandardizeTextures.desc': 'Enables Color and Alpha on every texture, sets the blend method to Multiply'
                                '\nand changes the materials transparency to Z-Transparency',
    'StandardizeTextures.success': 'All textures are now standardized.',

    'CombineMaterialsButton.label': 'Combine Same Materials',
    'CombineMaterialsButton.desc': 'Combines similar materials into one, reducing draw calls.\n'
                                   'Your avatar should visibly look the same after this operation.\n'
                                   'This is a very important step for optimizing your avatar.\n'
                                   'If you have problems with this, please tell us!\n',
    'CombineMaterialsButton.error.noChanges': 'No materials combined.',
    'CombineMaterialsButton.success': 'Combined {number} materials!',

    'ConvertAllToPngButton.label': 'Convert Textures to PNG',
    'ConvertAllToPngButton.desc': 'Converts all texture files into PNG files.'
                                  '\nThis helps with transparency and compatibility issues.'
                                  '\n\nThe converted image files will be saved next to the old ones',
    'ConvertAllToPngButton.success': 'Converted {number} to PNG files.',

    # Tools Root bone
    'RootButton.label': 'Parent Bones',
    'RootButton.desc': 'This will duplicate the parent of the bones and reparent them to the duplicate.\n'
                       'Very useful for Dynamic Bones.',
    'RootButton.success': 'Bones parented!',

    'RefreshRootButton.label': 'Refresh List',
    'RefreshRootButton.desc': 'This will clear the group bones list cache and rebuild it, useful if bones have changed or your model.',
    'RefreshRootButton.success': 'Root bones refreshed, check the root bones list again.',

    # Tools Settings
    'RevertChangesButton.label': 'Revert Settings',
    'RevertChangesButton.desc': 'Revert the changes back to how they were on Blender start-up.',
    'RevertChangesButton.success': 'Settings reverted.',

    'ResetGoogleDictButton.label': 'Clear Local Google Translations',
    'ResetGoogleDictButton.desc': 'Deletes all currently saved Google Translations. You can\'t undo this',
    'ResetGoogleDictButton.resetInfo': 'Local Google Dictionary cleared!',

    'DebugTranslations.label': 'Debug Google Translations',  # DEV ONLY
    'DebugTranslations.desc': 'Tests Google translations and prints the response into a file called \'google-response.txt\' located in the cats addon folder > resources'
                              '\nThis button is only visible in the cats development version',  # DEV ONLY
    'DebugTranslations.error': 'Errors found, response printed!!',  # DEV ONLY
    'DebugTranslations.success': 'No issues with Google Translations found, response printed!',  # DEV ONLY

    # Tools Shapekey
    'ShapeKeyApplier.label': 'Apply Selected Shapekey to Basis',
    'ShapeKeyApplier.desc': 'Applies the selected shape key to the new Basis at it\'s current strength and creates a reverted shape key from the selected one',
    'ShapeKeyApplier.error.revertCustomBasis': ['To revert the shape keys, please apply the "Reverted" shape keys in reverse order.',
                                                'Start with the shape key called "{name}".',
                                                '',
                                                'If you didn\'t change the shape key order, you can revert the shape keys from top to bottom.'],
    'ShapeKeyApplier.error.revertCustomBasis.scale': 7.3,
    'ShapeKeyApplier.error.revert': ['To revert the shape keys, please apply the "Reverted" shape keys in reverse order.',
                                     'Start with the reverted shape key that uses the relative key called "Basis".',
                                     '',
                                     "If you didn't change the shape key order, you can revert the shape keys from top to bottom."],
    'ShapeKeyApplier.error.revert.scale': 7.3,
    'ShapeKeyApplier.successRemoved': 'Successfully removed shapekey "{name}" from the Basis.',
    'ShapeKeyApplier.successSet': 'Successfully set shapekey "{name}" as the new Basis.',

    'addToShapekeyMenu.ShapeKeyApplier.label': 'Apply Selected Shapekey to Basis',

    # Tools Supporter
    'PatreonButton.label': 'Become a Patron',
    'PatreonButton.URL': 'https://www.patreon.com/catsblenderplugin',
    'PatreonButton.success': 'Patreon page opened.',

    'ReloadButton.label': 'Reload List',
    'ReloadButton.desc': 'Reloads the supporter list',

    'DynamicPatronButton.label': 'Supporter Name',
    'DynamicPatronButton.desc': 'This is an awesome supporter',

    'register_dynamic_buttons.desc': '{name} is an awesome supporter',

    # Tools Translate
    'TranslateShapekeyButton.label': 'Translate Shape Keys',
    'TranslateShapekeyButton.desc': 'Translates all shape keys using the internal dictionary and Google Translate',
    'TranslateShapekeyButton.success': 'Translated {number} shape keys.',

    'TranslateBonesButton.label': 'Translate Bones',
    'TranslateBonesButton.desc': 'Translates all bones using the internal dictionary and Google Translate',
    'TranslateBonesButton.success': 'Translated {number} bones.',

    'TranslateObjectsButton.label': 'Translate Meshes & Objects',
    'TranslateObjectsButton.desc': 'Translates all meshes and objects using the internal dictionary and Google Translate',
    'TranslateObjectsButton.success': 'Translated {number} meshes and objects.',

    'TranslateMaterialsButton.label': 'Translate Materials',
    'TranslateMaterialsButton.desc': 'Translates all materials using the internal dictionary and Google Translate',
    'TranslateMaterialsButton.success': 'Translated {number} materials.',

    'TranslateTexturesButton.label': 'Translate Textures',
    'TranslateTexturesButton.desc': 'Translates all textures using the internal dictionary and Google Translate',
    'TranslateTexturesButton.success_alt': 'Translated all textures',
    'TranslateTexturesButton.error.noInternet': 'Could not connect to Google. Please check your internet connection.',
    'TranslateTexturesButton.success': 'Translated {number} textures',

    'TranslateAllButton.label': 'Translate Everything',
    'TranslateAllButton.desc': 'Translates everything using the internal dictionary and Google Translate',
    'TranslateAllButton.success': 'Translated everything.',

    'TranslateX.error.wrongVersion': 'You need Blender 2.79 or higher for this function.',

    'update_dictionary.error.cantConnect': 'Could not connect to Google. Some parts could not be translated.',
    'update_dictionary.error.temporaryBan': 'It looks like you got banned from Google Translate temporarily!',
    'update_dictionary.error.catsTranslated': '\nCats translated what it could with the local dictionary, but you will have to try again later for the Google translations.',
    'update_dictionary.error.cantAccess': 'Cats was not able to access Google Translate!',
    'update_dictionary.error.errorMsg': 'You got an error message from Google Translate!',
    'update_dictionary.error.apiChanged': 'Could not get translations from Google Translate!'
                                          '\nThis means that Google changed their API and translations will no longer work until this is fixed.'
                                          '\nPlease translate manually or wait for an CATS update.'
                                          '\nFor updates and dicussions please join our Discord. The link can be found in the Credits panel down below.',

    # Tools Viseme
    'AutoVisemeButton.label': 'Create Visemes',
    'AutoVisemeButton.desc': 'This will give your avatar the ability to mimic each sound that comes from your mouth by blending between various shapes to mimic your actual voice.\n'
                             'It will generate 15 shape keys from the 3 shape keys you specify',
    'AutoVisemeButton.error.noShapekeys': 'This mesh has no shapekeys!',
    'AutoVisemeButton.error.selectShapekeys': 'Please select the correct mouth shapekeys instead of "Basis"!',
    'AutoVisemeButton.success': 'Created mouth visemes!',

    # Extensions
    'Scene.armature.label': 'Armature',
    'Scene.armature.desc': 'Select the armature which will be used by Cats',

    'Scene.zip_content.label': 'Zip Content',
    'Scene.zip_content.desc': 'Select the model you want to import',

    'Scene.keep_upper_chest.label': 'Keep Upper Chest',
    'Scene.keep_upper_chest.desc': 'VRChat now partially supports the Upper Chest bone, so deleting it is no longer necessary.'
                                   '\n\nWARNING: Currently this breaks Eye Tracking, so don\'t check this if you want Eye Tracking',

    'Scene.combine_mats.label': 'Combine Same Materials',
    'Scene.combine_mats.desc': 'Combines similar materials into one, reducing draw calls.\n\n'
                               'Your avatar should visibly look the same after this operation.\n'
                               'This is a very important step for optimizing your avatar.\n'
                               'If you have problems with this, uncheck this option and tell us!\n',

    'Scene.remove_zero_weight.label': 'Remove Zero Weight Bones',
    'Scene.remove_zero_weight.desc': 'Cleans up the bones hierarchy, deleting all bones that don\'t directly affect any vertices.'
                                     '\nUncheck this if bones or vertex groups that you want to keep got deleted',

    'Scene.keep_end_bones.label': 'Keep End Bones',
    'Scene.keep_end_bones.desc': 'Saves end bones from deletion.'
                                 '\n\nThis can improve skirt movement for dynamic bones, but increases the bone count.'
                                 '\nThis can also fix issues with crumbled finger bones in Unity.'
                                 '\nMake sure to always uncheck "Add Leaf Bones" when exporting or use the CATS export button',

    'Scene.keep_twist_bones.label': 'Keep Twist Bones',
    'Scene.keep_twist_bones.desc': 'This will keep any bone with "Twist" in the name.'
                                   '\nSo if there are certain bones that you want to keep, you can add "Twist" to them and they won\'t get deleted.'
                                   '\n\nVRChat can now make use of twist bones, so you can use this option to keep them',

    'Scene.fix_twist_bones.label': 'Fix MMD Twist Bones',
    'Scene.fix_twist_bones.desc': 'This will make MMD arm twist bones usable in VRChat.'
                                  '\nWIll only work if the twist bones are properly named.'
                                  '\nRequired names:'
                                  '\n  - ArmTwist[1-3]_[L/R]'
                                  '\n  - HandTwist[1-3]_[L/R]'
                                  '\n\nYou don\'t need to enable "Keep Twist Bones" for this to work',

    'Scene.join_meshes.label': 'Join Meshes',
    'Scene.join_meshes.desc': 'Joins all meshes of this model together.'
                              '\nIt also:'
                              '\n  - Applies all transformations'
                              '\n  - Repairs broken armature modifiers'
                              '\n  - Applies all decimation and mirror modifiers'
                              '\n  - Merges UV maps correctly'
                              '\n'
                              '\nINFO: You should always join your meshes',

    'Scene.connect_bones.label': 'Connect Bones',
    'Scene.connect_bones.desc': 'This connects all bones to their child bone if they have exactly one child bone.\n'
                                'This will not change how the bones function in any way, it just improves the aesthetic of the armature',

    'Scene.fix_materials.label': 'Fix Materials',
    'Scene.fix_materials.desc': 'This will apply some VRChat related fixes to materials',

    'Scene.remove_rigidbodies_joints.label': 'Remove Rigidbodies and Joints',
    'Scene.remove_rigidbodies_joints.desc': 'Rigidbodies and joints are used by MMD software to simulate physics.'
                                            '\nThey are completely useless for VRChat, so removing them is recommended for VRChat users!',

    'Scene.use_google_only.label': 'Use Old Translations (not recommended)',
    'Scene.use_google_only.desc': 'Ignores the internal dictionary and only uses the Google Translator for shape key translations.'
                                  '\n'
                                  '\nThis will result in slower translation speed and worse translations, but the translations will be like in CATS version 0.9.0 and older.'
                                  '\nOnly use this if you have animations which rely on the old translations and you don\'t want to convert them to the new ones',

    'Scene.show_more_options.label': 'Show More Options',
    'Scene.show_more_options.desc': 'Shows more model options',

    'Scene.merge_mode.label': 'Merge Mode',
    'Scene.merge_mode.desc': 'Mode',
    'Scene.merge_mode.armature.label': 'Merge Armatures',
    'Scene.merge_mode.armature.desc': 'Here you can merge two armatures together.',
    'Scene.merge_mode.mesh.label': 'Attach Mesh',
    'Scene.merge_mode.mesh.desc': 'Here you can attach a mesh to an armature.',

    'Scene.merge_armature_into.label': 'Base Armature',
    'Scene.merge_armature_into.desc': 'Select the armature into which the other armature will be merged\n',

    'Scene.merge_armature.label': 'Merge Armature',
    'Scene.merge_armature.desc': 'Select the armature which will be merged into the selected armature above\n',

    'Scene.attach_to_bone.label': 'Attach to Bone',
    'Scene.attach_to_bone.desc': 'Select the bone to which the armature will be attached to\n',

    'Scene.attach_mesh.label': 'Attach Mesh',
    'Scene.attach_mesh.desc': 'Select the mesh which will be attached to the selected bone in the selected armature\n',

    'Scene.merge_same_bones.label': 'Merge All Bones',
    'Scene.merge_same_bones.desc': 'Merges all bones together that have the same name instead of only the base bones (Hips, Spine, etc).'
                                   '\nYou will have to make sure that all the bones you want to merge have the same name.'
                                   '\n'
                                   '\nIf this is checked, you won\'t need to fix the model with CATS beforehand but it is still advised to do so.'
                                   '\nIf this is unchecked, CATS will only merge the base bones (Hips, Spine, etc).'
                                   '\n'
                                   '\nThis can have unintended side effects, so check your model afterwards!'
                                   '\n',

    'Scene.apply_transforms.label': 'Apply Transforms',
    'Scene.apply_transforms.desc': 'Check this if both armatures and meshes are already at their correct positions.'
                                   '\nThis will cause them to stay exactly where they are when merging',

    'Scene.merge_armatures_join_meshes.label': 'Join Meshes',
    'Scene.merge_armatures_join_meshes.desc': 'This will join all meshes.'
                                              '\nNot checking this will always apply transforms',

    'Scene.merge_armatures_remove_zero_weight_bones.label': 'Remove Zero Weight Bones',
    'Scene.merge_armatures_remove_zero_weight_bones.desc': 'Cleans up the bones hierarchy, deleting all bones that don\'t directly affect any vertices.'
                                                           '\nUncheck this if bones or vertex groups that you want to keep got deleted',

    # Decimation
    'Scene.decimation_mode.label': 'Decimation Mode',
    'Scene.decimation_mode.desc': 'Decimation Mode',
    'Scene.decimation_mode.smart.label': "Smart",
    'Scene.decimation_mode.smart.desc': 'Best results - repair shape keys after decimation\n'
                                        '\n'
                                        "This will decimate your whole model and attempt to undo the warping caused by Blender's decimation.\n"
                                        "This will give the best results and keep blinking and lip syncing, but may have issues on some models.",
    'Scene.decimation_mode.safe.label': 'Safe',
    'Scene.decimation_mode.safe.desc': 'Decent results - no shape key loss\n'
                                       '\n'
                                       'This will only decimate meshes with no shape keys.\n'
                                       'The results are decent and you won\'t lose any shape keys.\n'
                                       'Eye Tracking and Lip Syncing will be fully preserved.',
    'Scene.decimation_mode.half.label': 'Half',
    'Scene.decimation_mode.half.desc': 'Good results - minimal shape key loss\n'
                                       '\n'
                                       'This will only decimate meshes with less than 4 shape keys as those are often not used.\n'
                                       'The results are better but you will lose the shape keys in some meshes.\n'
                                       'Eye Tracking and Lip Syncing should still work.',
    'Scene.decimation_mode.full.label': 'Full',
    'Scene.decimation_mode.full.desc': 'Consistent results - full shape key loss\n'
                                       '\n'
                                       'This will decimate your whole model deleting all shape keys in the process.\n'
                                       'This will give consistent results but you will lose the ability to add blinking and Lip Syncing.\n'
                                       'Eye Tracking will still work if you disable Eye Blinking.',
    'Scene.decimation_mode.custom.label': 'Custom',
    'Scene.decimation_mode.custom.desc': 'Custom results - custom shape key loss\n'
                                         '\n'
                                         'This will let you choose which meshes and shape keys should not be decimated.\n',

    'Scene.selection_mode.label': 'Selection Mode',
    'Scene.selection_mode.desc': 'Selection Mode',
    'Scene.selection_mode.shapekeys.label': 'Shape Keys',
    'Scene.selection_mode.shapekeys.desc': 'Select all the shape keys you want to preserve here.',
    'Scene.selection_mode.meshes.label': 'Meshes',
    'Scene.selection_mode.meshes.desc': 'Select all the meshes you don\'t want to decimate here.',

    'Scene.add_shape_key.label': 'Shape',
    'Scene.add_shape_key.desc': 'The shape key you want to keep',

    'Scene.add_mesh.label': 'Mesh',
    'Scene.add_mesh.desc': 'The mesh you want to leave untouched by the decimation',

    'Scene.decimate_fingers.label': 'Save Fingers',
    'Scene.decimate_fingers.desc': 'Check this if you don\'t want to decimate your fingers!\n'
                                   'Results will be worse but there will be no issues with finger movement.\n'
                                   'This is probably only useful if you have a VR headset.\n'
                                   '\n'
                                   'This operation requires the finger bones to be named specifically:\n'
                                   'Thumb(0-2)_(L/R)\n'
                                   'IndexFinger(1-3)_(L/R)\n'
                                   'MiddleFinger(1-3)_(L/R)\n'
                                   'RingFinger(1-3)_(L/R)\n'
                                   'LittleFinger(1-3)_(L/R)',

    'Scene.decimate_hands.label': 'Save Hands',
    'Scene.decimate_hands.desc': 'Check this if you don\'t want to decimate your full hands!\n'
                                 'Results will be worse but there will be no issues with hand movement.\n'
                                 'This is probably only useful if you have a VR headset.\n'
                                 '\n'
                                 'This operation requires the finger and hand bones to be named specifically:\n'
                                 'Left/Right wrist\n'
                                 'Thumb(0-2)_(L/R)\n'
                                 'IndexFinger(1-3)_(L/R)\n'
                                 'MiddleFinger(1-3)_(L/R)\n'
                                 'RingFinger(1-3)_(L/R)\n'
                                 'LittleFinger(1-3)_(L/R)',

    'Scene.decimation_remove_doubles.label': 'Remove Doubles',
    'Scene.decimation_remove_doubles.desc': 'Uncheck this if you got issues with with this checked',
    'Scene.decimation_animation_weighting.label': "Animation weighting",
    'Scene.decimation_animation_weighting.desc': "Weight decimation based on shape keys and vertex group overlap\n"
                                                 "Results in better animating topology by trading off overall shape accuracy\n"
                                                 "Use if your elbows/joints end up with bad topology",
    'Scene.decimation_animation_weighting_factor.label': "Factor",
    'Scene.decimation_animation_weighting_factor.desc': "How much influence the animation weighting has on the overall shape",

    'Scene.max_tris.label': 'Tris',
    'Scene.max_tris.desc': 'The target amount of tris after decimation',

    # Eye Tracking
    'Scene.eye_mode.label': 'Eye Mode',
    'Scene.eye_mode.desc': 'Mode',
    'Scene.eye_mode.creation.label': 'Creation',
    'Scene.eye_mode.creation.desc': 'Here you can create eye tracking.',
    'Scene.eye_mode.testing.label': 'Testing',
    'Scene.eye_mode.testing.desc': 'Here you can test how eye tracking will look in-game.',

    'Scene.mesh_name_eye.label': 'Mesh',
    'Scene.mesh_name_eye.desc': 'The mesh with the eyes vertex groups',

    'Scene.head.label': 'Head',
    'Scene.head.desc': 'The head bone containing the eye bones',

    'Scene.eye_left.label': 'Left Eye',
    'Scene.eye_left.desc': 'The models left eye bone',

    'Scene.eye_right.label': 'Right Eye',
    'Scene.eye_right.desc': 'The models right eye bone',

    'Scene.wink_left.label': 'Blink Left',
    'Scene.wink_left.desc': 'The shape key containing a blink with the left eye',

    'Scene.wink_right.label': 'Blink Right',
    'Scene.wink_right.desc': 'The shape key containing a blink with the right eye',

    'Scene.lowerlid_left.label': 'Lowerlid Left',
    'Scene.lowerlid_left.desc': 'The shape key containing a slightly raised left lower lid.\n'
                                'Can be set to "Basis" to disable lower lid movement',

    'Scene.lowerlid_right.label': 'Lowerlid Right',
    'Scene.lowerlid_right.desc': 'The shape key containing a slightly raised right lower lid.\n'
                                 'Can be set to "Basis" to disable lower lid movement',

    'Scene.disable_eye_movement.label': 'Disable Eye Movement',
    'Scene.disable_eye_movement.desc': 'IMPORTANT: Do your decimation first if you check this!\n'
                                       '\n'
                                       'Disables eye movement. Useful if you only want blinking.\n'
                                       'This creates eye bones with no movement bound to them.\n'
                                       'You still have to assign "LeftEye" and "RightEye" to the eyes in Unity',

    'Scene.disable_eye_blinking.label': 'Disable Eye Blinking',
    'Scene.disable_eye_blinking.desc': 'Disables eye blinking. Useful if you only want eye movement.\n'
                                       'This will create the necessary shape keys but leaves them empty',

    'Scene.eye_distance.label': 'Eye Movement Range',
    'Scene.eye_distance.desc': 'Higher = more eye movement\n'
                               'Lower = less eye movement\n'
                               'Warning: Too little or too much range can glitch the eyes.\n'
                               'Test your results in the "Eye Testing"-Tab!\n',

    'Scene.eye_rotation_x.label': 'Up - Down',
    'Scene.eye_rotation_x.desc': 'Rotate the eye bones on the vertical axis',

    'Scene.eye_rotation_y.label': 'Left - Right',
    'Scene.eye_rotation_y.desc': 'Rotate the eye bones on the horizontal axis.'
                                 '\nThis is from your own point of view',

    'Scene.iris_height.label': 'Iris Height',
    'Scene.iris_height.desc': 'Moves the iris away from the eye ball',

    'Scene.eye_blink_shape.label': 'Blink Strength',
    'Scene.eye_blink_shape.desc': 'Test the blinking of the eye',

    'Scene.eye_lowerlid_shape.label': 'Lowerlid Strength',
    'Scene.eye_lowerlid_shape.desc': 'Test the lowerlid blinking of the eye',

    'Scene.mesh_name_viseme.label': 'Mesh',
    'Scene.mesh_name_viseme.desc': 'The mesh with the mouth shape keys',

    # Visemes
    'Scene.mouth_a.label': 'Viseme AA',
    'Scene.mouth_a.desc': 'Shape key containing mouth movement that looks like someone is saying "aa".\nDo not put empty shape keys like "Basis" in here',

    'Scene.mouth_o.label': 'Viseme OH',
    'Scene.mouth_o.desc': 'Shape key containing mouth movement that looks like someone is saying "oh".\nDo not put empty shape keys like "Basis" in here',

    'Scene.mouth_ch.label': 'Viseme CH',
    'Scene.mouth_ch.desc': 'Shape key containing mouth movement that looks like someone is saying "ch". Opened lips and clenched teeth.\nDo not put empty shape keys like "Basis" in here',

    'Scene.shape_intensity.label': 'Shape Key Mix Intensity',
    'Scene.shape_intensity.desc': 'Controls the strength in the creation of the shape keys. Lower for less mouth movement strength',

    # Bone Parenting
    'Scene.root_bone.label': 'To Parent',
    'Scene.root_bone.desc': 'List of bones that look like they could be parented together to a root bone',

    # Optimize
    'Scene.optimize_mode.label': 'Optimize Mode',
    'Scene.optimize_mode.desc': 'Mode',
    'Scene.optimize_mode.atlas.label': 'Atlas',
    'Scene.optimize_mode.atlas.desc': 'Allows you to make a texture atlas.',
    'Scene.optimize_mode.material.label': 'Material',
    'Scene.optimize_mode.material.desc': 'Some various options on material manipulation.',
    'Scene.optimize_mode.bonemerging.label': 'Bone Merging',
    'Scene.optimize_mode.bonemerging.desc': 'Allows child bones to be merged into their parents.',

    # Bone Merging
    'Scene.merge_ratio.label': 'Merge Ratio',
    'Scene.merge_ratio.desc': 'Higher = more bones will be merged\n'
                              'Lower = less bones will be merged\n',

    'Scene.merge_mesh.label': 'Mesh',
    'Scene.merge_mesh.desc': 'The mesh with the bones vertex groups',

    'Scene.merge_bone.label': 'To Merge',
    'Scene.merge_bone.desc': 'List of bones that look like they could be merged together to reduce overall bones',

    # Settings
    'Scene.show_mmd_tabs.label': 'Show mmd_tools tabs',
    'Scene.show_mmd_tabs.desc': 'Allows you to hide/show the mmd_tools tabs "MMD" and "Misc"',

    'Scene.embed_textures.label': 'Embed Textures on Export',
    'Scene.embed_textures.desc': 'Enable this to embed the texture files into the FBX file upon export.'
                                 '\nUnity will automatically extract these textures and put them into a separate folder.'
                                 '\nThis might not work for everyone and it increases the file size of the exported FBX file',

    'Scene.use_custom_mmd_tools.label': 'Use Custom mmd_tools',
    'Scene.use_custom_mmd_tools.desc': 'Enable this to use your own version of mmd_tools. This will disable the internal cats mmd_tools',

    'Scene.debug_translations.label': 'Debug Google Translations',
    'Scene.debug_translations.desc': 'Tests the Google Translations and prints the Google response in case of error',

    # Bake
    'Scene.bake_resolution.label': "Resolution",
    'Scene.bake_resolution.desc': "Output resolution for the textures.\n"
                                  "- 2048 is typical for desktop use.\n"
                                  "- 1024 is reccomended for the Quest",
    'Scene.bake_use_decimation.label': 'Decimate',
    'Scene.bake_use_decimation.desc': 'Reduce polycount before baking, then use Normal maps to restore detail',
    'Scene.bake_generate_uvmap.label': 'Generate UVMap',
    'Scene.bake_generate_uvmap.desc': "Re-pack islands for your mesh to a new non-overlapping UVMap.\n"
                                      "Only disable if your UVs are non-overlapping already.\n"
                                      "This will leave any map named \"Detail Map\" alone.\n"
                                      "Uses UVPackMaster where available for more efficient UVs, make sure the window is showing",
    'Scene.bake_uv_overlap_correction.label': "Overlap correction",
    'Scene.bake_uv_overlap_correction.desc': "Method used to prevent overlaps in UVMap",
    'Scene.bake_prioritize_face.label': 'Prioritize Head/Eyes',
    'Scene.bake_prioritize_face.desc': 'Scale any UV islands attached to the head/eyes by a given factor.',
    'Scene.bake_face_scale.label': "Head/Eyes Scale",
    'Scene.bake_face_scale.desc': "How much to scale up the face/eyes portion of the textures.",
    'Scene.bake_quick_compare.label': 'Quick compare',
    'Scene.bake_quick_compare.desc': 'Move output avatar next to existing one to quickly compare',
    'Scene.bake_illuminate_eyes.label': 'Set eyes to full brightness',
    'Scene.bake_illuminate_eyes.desc': 'Relight LeftEye and RightEye to be full brightness.\n'
                                       "Without this, the eyes will have the shadow of the surrounding socket baked in,\n"
                                       "which doesn't animate well",
    'Scene.bake_pass_smoothness.label': 'Smoothness',
    'Scene.bake_pass_smoothness.desc': 'Bakes Roughness and then inverts the values.\n'
                                       'To use this, it needs to be packed to the Alpha channel of either Diffuse or Metallic.\n'
                                       'Not neccesary if your mesh has a global roughness value',
    'Scene.bake_pass_diffuse.label': 'Diffuse (Color)',
    'Scene.bake_pass_diffuse.desc': 'Bakes diffuse, un-lighted color. Usually you will want this.\n'
                                    'While baking, this temporarily links "Metallic" to "Anisotropic Rotation" as metallic can cause issues.',
    'Scene.bake_preserve_seams.label': "Preserve seams",
    'Scene.bake_preserve_seams.desc': 'Forces the Decimate operation to preserve vertices making up seams, preventing hard edges along seams.\n'
                                      'May result in less ideal geometry.\n'
                                      "Use if you notice ugly edges along your texture seams.",
    'Scene.bake_pass_normal.label': 'Normal (Bump)',
    'Scene.bake_pass_normal.desc': "Bakes a normal (bump) map. Allows you to keep the shading of a complex object with\n"
                                   "the geometry of a simple object. If you have selected 'Decimate', it will create a map\n"
                                   "that makes the low res output look like the high res input.\n"
                                   "Will not work well if you have self-intersecting islands",
    'Scene.bake_normal_apply_trans.label': 'Apply transforms',
    'Scene.bake_normal_apply_trans.desc': "Applies offsets while baking normals. Neccesary if your model has many materials with different normal maps\n"
                                          "Turn this off if applying location causes problems with your model",
    'Scene.bake_pass_ao.label': 'Ambient Occlusion',
    'Scene.bake_pass_ao.desc': 'Bakes Ambient Occlusion, non-projected shadows. Adds a significant amount of detail to your model.\n'
                               'Reccomended for non-toon style avatars.\n'
                               'Takes a fairly long time to bake',
    'Scene.bake_pass_questdiffuse.label': 'Quest Diffuse (Color+AO)',
    'Scene.bake_pass_questdiffuse.desc': 'Blends the result of the Diffuse and AO bakes to make Quest-compatible shading.',
    'Scene.bake_pass_emit.label': 'Emit',
    'Scene.bake_pass_emit.desc': 'Bakes Emit, glowyness',
    'Scene.bake_diffuse_alpha_pack.label': "Alpha Channel",
    'Scene.bake_diffuse_alpha_pack.desc': "What to pack to the Diffuse Alpha channel",
    'Scene.bake_metallic_alpha_pack.label': "Metallic Alpha Channel",
    'Scene.bake_metallic_alpha_pack.desc': "What to pack to the Metallic Alpha channel",
    'Scene.bake_pass_alpha.label': 'Transparency',
    'Scene.bake_pass_alpha.desc': 'Bakes transparency by connecting the last Principled BSDF Alpha input\n'
                                  'to the Base Color input and baking Diffuse.\n'
                                  'Not a native pass in Blender, results may vary\n'
                                  'Unused if you are baking to Quest',
    'Scene.bake_pass_metallic.label': 'Metallic',
    'Scene.bake_pass_metallic.desc': 'Bakes metallic by connecting the last Principled BSDF Metallic input\n'
                                     'to the Base Color input and baking Diffuse.\n'
                                     'Not a native pass in Blender, results may vary',
    'Scene.bake_questdiffuse_opacity.label': "AO Opacity",
    'Scene.bake_questdiffuse_opacity.desc': "The opacity of the shadows to blend onto the Diffuse map.\n"
                                            "This should match the unity slider for AO on the Desktop version.",

    "Scene.bake_uv_overlap_correction.none.label": "None",
    "Scene.bake_uv_overlap_correction.none.desc": "Leave islands as they are. Use if islands don't self-intersect at all",
    "Scene.bake_uv_overlap_correction.unmirror.label": "Unmirror",
    "Scene.bake_uv_overlap_correction.unmirror.desc": "Move all face islands with positive X values over one to un-pin mirrored UVs. Solves most UV pinning issues.",
    "Scene.bake_uv_overlap_correction.reproject.label": "Reproject",
    "Scene.bake_uv_overlap_correction.reproject.desc": "Use blender's Smart UV Project to come up with an entirely new island layout. Tends to reduce quality.",

    "Scene.bake_diffuse_alpha_pack.none.label": "None",
    "Scene.bake_diffuse_alpha_pack.none.desc": "No alpha channel",
    "Scene.bake_diffuse_alpha_pack.transparency.label": "Transparency",
    "Scene.bake_diffuse_alpha_pack.transparency.desc": "Pack Transparency",
    "Scene.bake_diffuse_alpha_pack.smoothness.label": "Smoothness",
    "Scene.bake_diffuse_alpha_pack.smoothness.desc": "Pack Smoothness. Most efficient if you don't have transparency or metallic textures.",

    "Scene.bake_metallic_alpha_pack.none.label": "None",
    "Scene.bake_metallic_alpha_pack.none.desc": "No alpha channel",
    "Scene.bake_metallic_alpha_pack.smoothness.label": "Smoothness",
    "Scene.bake_metallic_alpha_pack.smoothness.desc": "Pack Smoothness. Use this if your Diffuse alpha channel is already populated with Transparency",

    "cats_bake.warn_missing_nodes": "A material in use isn't using Nodes, fix this in the Shading tab.",
    "cats_bake.preset_desktop.label": "Desktop",
    "cats_bake.preset_desktop.desc": "Preset for producing an Excellent-rated Desktop avatar, not accounting for bones.\n"
                                     "This will try to automatically detect which bake passes are relevant to your model",
    "cats_bake.preset_quest.label": 'Quest',
    "cats_bake.preset_quest.desc": "Preset for producing an Excellent-rated Quest avatar, not accounting for bones.\n"
                                   "This will try to automatically detect which bake passes are relevant to your model",
    'cats_bake.bake.label': 'Copy and Bake (SLOW!)',
    'cats_bake.bake.desc': "Perform the bake. Warning, this performs an actual render!\n"
                           "This will create a copy of your avatar to leave the original alone.\n"
                           "Depending on your machine and model, this could take an hour or more.\n"
                           "For each pass, any Value node in your materials labeled bake_<bakename> will be\n"
                           "set to 1.0, for more granular customization.",
    'cats_bake.error.no_meshes': "No meshes found!",
    'cats_bake.error.render_engine': "You need to set your render engine to Cycles first!",
    'cats_bake.error.render_disabled': "One or more of your armature's meshes have rendering disabled!",
    'cats_bake.info.success': "Success! Textures and model saved to \'CATS Bake\' folder next to your .blend file.",

    'cats_bake.tutorial_button.label': "How to use",
    'cats_bake.tutorial_button.desc': "This will open the Cats wiki page for the Bake panel",
    'cats_bake.tutorial_button.URL': "https://github.com/GiveMeAllYourCats/cats-blender-plugin/wiki/Bake",
    'cats_bake.tutorial_button.success': "Bake Tutorial opened.",

    # Updater
    'CheckForUpdateButton.label': 'Check now for Update',
    'CheckForUpdateButton.desc': 'Checks if a new update is available for CATS',

    'UpdateToLatestButton.label': 'Update Now',
    'UpdateToLatestButton.desc': 'Update CATS to the latest version',

    'UpdateToSelectedButton.label': 'Update to Selected version',
    'UpdateToSelectedButton.desc': 'Update CATS to the selected version',

    'UpdateToDevButton.label': 'Update to Development version',
    'UpdateToDevButton.desc': 'Update CATS to the Development version',

    'RemindMeLaterButton.label': 'Remind me later',
    'RemindMeLaterButton.desc': 'This hides the update notification \'til the next Blender restart',
    'RemindMeLaterButton.success': 'You will be reminded later',

    'IgnoreThisVersionButton.label': 'Ignore this version',
    'IgnoreThisVersionButton.desc': 'This ignores this version. You will be reminded again when the next version releases',
    'IgnoreThisVersionButton.success': 'Version {name} will be ignored.',

    'ShowPatchnotesPanel.label': '注释',
    'ShowPatchnotesPanel.desc': '显示所选版本的补丁说明',
    'ShowPatchnotesPanel.releaseDate': 'Released: {date}',

    'ConfirmUpdatePanel.label': '确认更新',
    'ConfirmUpdatePanel.desc': '这将显示一个面板，你必须在其中确认你的更新选择',
    'ConfirmUpdatePanel.warn.dev1': '警告:',
    'ConfirmUpdatePanel.warn.dev2': ' 如果CATS的开发版本（The development version of CATS if the place where）',
    'ConfirmUpdatePanel.warn.dev3': ' 我们测试新功能和错误修复。',
    'ConfirmUpdatePanel.warn.dev4': ' 这个版本可能有些功能非常不稳定',
    'ConfirmUpdatePanel.warn.dev5': ' 可能无法正常工作。',
    'ConfirmUpdatePanel.ShowPatchnotesPanel.label': '显示注释',
    'ConfirmUpdatePanel.updateNow': '现在更新:',

    'UpdateCompletePanel.label': '安装报告',
    'UpdateCompletePanel.desc': '现在更新已经完成',
    'UpdateCompletePanel.success1': 'CATS已成功更新。',
    'UpdateCompletePanel.success2': '重新启动Blender完成更新。',
    'UpdateCompletePanel.failure1': '更新失败。',
    'UpdateCompletePanel.failure2': '更多信息请参见更新器面板。',

    'UpdateNotificationPopup.label': '安装报告',
    'UpdateNotificationPopup.desc': '这将显示你有更新',
    'UpdateNotificationPopup.newUpdate': 'CATS v{name} 可用!',
    'UpdateNotificationPopup.ShowPatchnotesPanel.label': '显示注释',

    'check_for_update.cantCheck': '无法检查更新，稍后再试',

    'download_file.cantConnect': '无法连接到 Github',
    'download_file.cantFindZip': '找不到下载的zip压缩包',
    'download_file.cantFindCATS': '在下载的zip压缩包中找不到CATS',

    'draw_update_notification_panel.success': '重启Blender以完成更新!',
    'draw_update_notification_panel.newUpdate': 'CATS v{name} 可用!',
    'draw_update_notification_panel.UpdateToLatestButton.label': '立即更新',
    'draw_update_notification_panel.RemindMeLaterButton.label': '以后提醒我',
    'draw_update_notification_panel.IgnoreThisVersionButton.label': '忽略这个版本',

    'draw_updater_panel.updateLabel': '更新:',
    'draw_updater_panel.updateLabel_alt': 'CATS 更新器:',
    'draw_updater_panel.success': '重启Blender以完成更新!',
    'draw_updater_panel.CheckForUpdateButton.label': '检查中..',
    'draw_updater_panel.UpdateToLatestButton.label': '现在更新为 {name}',
    'draw_updater_panel.CheckForUpdateButton.label_alt': '立即查看更新',
    'draw_updater_panel.UpdateToLatestButton.label_alt': '最新的!',
    'draw_updater_panel.UpdateToSelectedButton.label': '安装版本:',
    'draw_updater_panel.UpdateToDevButton.label': '安装开发版',
    'draw_updater_panel.currentVersion': '当前版本: {name}',

    'bpy.types.Scene.cats_updater_version_list.label': 'Version',
    'bpy.types.Scene.cats_updater_version_list.desc': '选择您要安装的版本\n',

    'bpy.types.Scene.cats_update_action.label': '选择操作',
    'bpy.types.Scene.cats_update_action.desc': 'Action',
    'bpy.types.Scene.cats_update_action.update.label': '立即更新',
    'bpy.types.Scene.cats_update_action.update.desc': '现在更新到最新版本',
    'bpy.types.Scene.cats_update_action.ignore.label': '忽略这个版本',
    'bpy.types.Scene.cats_update_action.ignore.desc': '这忽略了这个版本。 当下一个版本发布时，会再次提醒您。',
    'bpy.types.Scene.cats_update_action.defer.label': '以后提醒我',
    'bpy.types.Scene.cats_update_action.defer.desc': '在下次重新启动Blender之前隐藏更新通知',

}
