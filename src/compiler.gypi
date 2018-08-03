# Copyright (c) 2013 The ANGLE Project Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
    'variables':
    {
        # These file lists are shared with the GN build.
        'angle_translator_sources':
        [
            '../include/EGL/egl.h',
            '../include/EGL/eglext.h',
            '../include/EGL/eglplatform.h',
            '../include/GLES2/gl2.h',
            '../include/GLES2/gl2ext.h',
            '../include/GLES2/gl2platform.h',
            '../include/GLES3/gl3.h',
            '../include/GLES3/gl3platform.h',
            '../include/GLES3/gl31.h',
            '../include/GLES3/gl32.h',
            '../include/GLSLANG/ShaderLang.h',
            '../include/GLSLANG/ShaderVars.h',
            '../include/KHR/khrplatform.h',
            '../include/angle_gl.h',
            'compiler/translator/BaseTypes.h',
            'compiler/translator/BuiltInFunctionEmulator.cpp',
            'compiler/translator/BuiltInFunctionEmulator.h',
            'compiler/translator/CallDAG.cpp',
            'compiler/translator/CallDAG.h',
            'compiler/translator/CodeGen.cpp',
            'compiler/translator/CollectVariables.cpp',
            'compiler/translator/CollectVariables.h',
            'compiler/translator/Common.h',
            'compiler/translator/Compiler.cpp',
            'compiler/translator/Compiler.h',
            'compiler/translator/ConstantUnion.cpp',
            'compiler/translator/ConstantUnion.h',
            'compiler/translator/Declarator.cpp',
            'compiler/translator/Declarator.h',
            'compiler/translator/Diagnostics.cpp',
            'compiler/translator/Diagnostics.h',
            'compiler/translator/DirectiveHandler.cpp',
            'compiler/translator/DirectiveHandler.h',
            'compiler/translator/ExtensionBehavior.cpp',
            'compiler/translator/ExtensionBehavior.h',
            'compiler/translator/FlagStd140Structs.cpp',
            'compiler/translator/FlagStd140Structs.h',
            'compiler/translator/FunctionLookup.cpp',
            'compiler/translator/FunctionLookup.h',
            'compiler/translator/HashNames.cpp',
            'compiler/translator/HashNames.h',
            'compiler/translator/ImmutableString.cpp',
            'compiler/translator/ImmutableString.h',
            'compiler/translator/ImmutableStringBuilder.cpp',
            'compiler/translator/ImmutableStringBuilder.h',
            'compiler/translator/InfoSink.cpp',
            'compiler/translator/InfoSink.h',
            'compiler/translator/Initialize.cpp',
            'compiler/translator/Initialize.h',
            'compiler/translator/InitializeDll.cpp',
            'compiler/translator/InitializeDll.h',
            'compiler/translator/InitializeGlobals.h',
            'compiler/translator/IntermNode.h',
            'compiler/translator/IntermNode.cpp',
            'compiler/translator/IsASTDepthBelowLimit.cpp',
            'compiler/translator/IsASTDepthBelowLimit.h',
            'compiler/translator/Operator.cpp',
            'compiler/translator/Operator.h',
            'compiler/translator/OutputTree.cpp',
            'compiler/translator/OutputTree.h',
            'compiler/translator/ParseContext.cpp',
            'compiler/translator/ParseContext.h',
            'compiler/translator/ParseContext_autogen.h',
            'compiler/translator/PoolAlloc.cpp',
            'compiler/translator/PoolAlloc.h',
            'compiler/translator/Pragma.h',
            'compiler/translator/QualifierTypes.h',
            'compiler/translator/QualifierTypes.cpp',
            'compiler/translator/Severity.h',
            'compiler/translator/ShaderLang.cpp',
            'compiler/translator/ShaderVars.cpp',
            'compiler/translator/StaticType.h',
            'compiler/translator/Symbol.cpp',
            'compiler/translator/Symbol.h',
            'compiler/translator/SymbolTable.cpp',
            'compiler/translator/SymbolTable.h',
            'compiler/translator/SymbolTable_autogen.cpp',
            'compiler/translator/SymbolTable_autogen.h',
            'compiler/translator/SymbolUniqueId.cpp',
            'compiler/translator/SymbolUniqueId.h',
            'compiler/translator/Types.cpp',
            'compiler/translator/Types.h',
            'compiler/translator/ValidateGlobalInitializer.cpp',
            'compiler/translator/ValidateGlobalInitializer.h',
            'compiler/translator/ValidateLimitations.cpp',
            'compiler/translator/ValidateLimitations.h',
            'compiler/translator/ValidateMaxParameters.h',
            'compiler/translator/ValidateMaxParameters.cpp',
            'compiler/translator/ValidateOutputs.cpp',
            'compiler/translator/ValidateOutputs.h',
            'compiler/translator/ValidateSwitch.cpp',
            'compiler/translator/ValidateSwitch.h',
            'compiler/translator/ValidateVaryingLocations.cpp',
            'compiler/translator/ValidateVaryingLocations.h',
            'compiler/translator/VariablePacker.cpp',
            'compiler/translator/VariablePacker.h',
            'compiler/translator/blocklayout.cpp',
            'compiler/translator/blocklayout.h',
            'compiler/translator/glslang.h',
            'compiler/translator/glslang.l',
            'compiler/translator/glslang.y',
            'compiler/translator/glslang_lex.cpp',
            'compiler/translator/glslang_tab.cpp',
            'compiler/translator/glslang_tab.h',
            'compiler/translator/length_limits.h',
            'compiler/translator/util.cpp',
            'compiler/translator/util.h',
            'compiler/translator/tree_ops/AddAndTrueToLoopCondition.cpp',
            'compiler/translator/tree_ops/AddAndTrueToLoopCondition.h',
            'compiler/translator/tree_ops/BreakVariableAliasingInInnerLoops.cpp',
            'compiler/translator/tree_ops/BreakVariableAliasingInInnerLoops.h',
            'compiler/translator/tree_ops/ClampFragDepth.cpp',
            'compiler/translator/tree_ops/ClampFragDepth.h',
            'compiler/translator/tree_ops/ClampPointSize.cpp',
            'compiler/translator/tree_ops/ClampPointSize.h',
            'compiler/translator/tree_ops/DeclareAndInitBuiltinsForInstancedMultiview.h',
            'compiler/translator/tree_ops/DeclareAndInitBuiltinsForInstancedMultiview.cpp',
            'compiler/translator/tree_ops/DeferGlobalInitializers.cpp',
            'compiler/translator/tree_ops/DeferGlobalInitializers.h',
            'compiler/translator/tree_ops/EmulateGLFragColorBroadcast.cpp',
            'compiler/translator/tree_ops/EmulateGLFragColorBroadcast.h',
            'compiler/translator/tree_ops/EmulatePrecision.cpp',
            'compiler/translator/tree_ops/EmulatePrecision.h',
            'compiler/translator/tree_ops/ExpandIntegerPowExpressions.cpp',
            'compiler/translator/tree_ops/ExpandIntegerPowExpressions.h',
            'compiler/translator/tree_ops/FoldExpressions.cpp',
            'compiler/translator/tree_ops/FoldExpressions.h',
            'compiler/translator/tree_ops/InitializeVariables.cpp',
            'compiler/translator/tree_ops/InitializeVariables.h',
            'compiler/translator/tree_ops/NameEmbeddedUniformStructs.cpp',
            'compiler/translator/tree_ops/NameEmbeddedUniformStructs.h',
            'compiler/translator/tree_ops/PruneEmptyCases.cpp',
            'compiler/translator/tree_ops/PruneEmptyCases.h',
            'compiler/translator/tree_ops/PruneNoOps.cpp',
            'compiler/translator/tree_ops/PruneNoOps.h',
            'compiler/translator/tree_ops/RecordConstantPrecision.cpp',
            'compiler/translator/tree_ops/RecordConstantPrecision.h',
            'compiler/translator/tree_ops/RegenerateStructNames.cpp',
            'compiler/translator/tree_ops/RegenerateStructNames.h',
            'compiler/translator/tree_ops/RemoveArrayLengthMethod.cpp',
            'compiler/translator/tree_ops/RemoveArrayLengthMethod.h',
            'compiler/translator/tree_ops/RemoveInvariantDeclaration.cpp',
            'compiler/translator/tree_ops/RemoveInvariantDeclaration.h',
            'compiler/translator/tree_ops/RemovePow.cpp',
            'compiler/translator/tree_ops/RemovePow.h',
            'compiler/translator/tree_ops/RemoveUnreferencedVariables.cpp',
            'compiler/translator/tree_ops/RemoveUnreferencedVariables.h',
            'compiler/translator/tree_ops/RewriteAtomicFunctionExpressions.cpp',
            'compiler/translator/tree_ops/RewriteAtomicFunctionExpressions.h',
            'compiler/translator/tree_ops/RewriteDoWhile.cpp',
            'compiler/translator/tree_ops/RewriteDoWhile.h',
            'compiler/translator/tree_ops/RewriteStructSamplers.cpp',
            'compiler/translator/tree_ops/RewriteStructSamplers.h',
            'compiler/translator/tree_ops/RewriteRepeatedAssignToSwizzled.cpp',
            'compiler/translator/tree_ops/RewriteRepeatedAssignToSwizzled.h',
            'compiler/translator/tree_ops/RewriteTexelFetchOffset.cpp',
            'compiler/translator/tree_ops/RewriteTexelFetchOffset.h',
            'compiler/translator/tree_ops/RewriteUnaryMinusOperatorFloat.cpp',
            'compiler/translator/tree_ops/RewriteUnaryMinusOperatorFloat.h',
            'compiler/translator/tree_ops/RewriteUnaryMinusOperatorInt.cpp',
            'compiler/translator/tree_ops/RewriteUnaryMinusOperatorInt.h',
            'compiler/translator/tree_ops/ScalarizeVecAndMatConstructorArgs.cpp',
            'compiler/translator/tree_ops/ScalarizeVecAndMatConstructorArgs.h',
            'compiler/translator/tree_ops/SeparateDeclarations.cpp',
            'compiler/translator/tree_ops/SeparateDeclarations.h',
            'compiler/translator/tree_ops/SimplifyLoopConditions.cpp',
            'compiler/translator/tree_ops/SimplifyLoopConditions.h',
            'compiler/translator/tree_ops/SplitSequenceOperator.cpp',
            'compiler/translator/tree_ops/SplitSequenceOperator.h',
            'compiler/translator/tree_ops/UnfoldShortCircuitAST.cpp',
            'compiler/translator/tree_ops/UnfoldShortCircuitAST.h',
            'compiler/translator/tree_ops/UseInterfaceBlockFields.cpp',
            'compiler/translator/tree_ops/UseInterfaceBlockFields.h',
            'compiler/translator/tree_ops/VectorizeVectorScalarArithmetic.cpp',
            'compiler/translator/tree_ops/VectorizeVectorScalarArithmetic.h',
            'compiler/translator/tree_util/BuiltIn_autogen.h',
            'compiler/translator/tree_util/FindMain.cpp',
            'compiler/translator/tree_util/FindMain.h',
            'compiler/translator/tree_util/FindSymbolNode.cpp',
            'compiler/translator/tree_util/FindSymbolNode.h',
            'compiler/translator/tree_util/IntermNodePatternMatcher.cpp',
            'compiler/translator/tree_util/IntermNodePatternMatcher.h',
            'compiler/translator/tree_util/IntermNode_util.cpp',
            'compiler/translator/tree_util/IntermNode_util.h',
            'compiler/translator/tree_util/IntermTraverse.cpp',
            'compiler/translator/tree_util/IntermTraverse.h',
            'compiler/translator/tree_util/NodeSearch.h',
            'compiler/translator/tree_util/ReplaceVariable.cpp',
            'compiler/translator/tree_util/ReplaceVariable.h',
            'compiler/translator/tree_util/RunAtTheEndOfShader.cpp',
            'compiler/translator/tree_util/RunAtTheEndOfShader.h',
            'compiler/translator/tree_util/Visit.h',
            'third_party/compiler/ArrayBoundsClamper.cpp',
            'third_party/compiler/ArrayBoundsClamper.h',
        ],
        'angle_translator_essl_sources':
        [
            'compiler/translator/OutputESSL.cpp',
            'compiler/translator/OutputESSL.h',
            'compiler/translator/TranslatorESSL.cpp',
            'compiler/translator/TranslatorESSL.h',
        ],
        'angle_translator_glsl_sources':
        [
            'compiler/translator/BuiltInFunctionEmulatorGLSL.cpp',
            'compiler/translator/BuiltInFunctionEmulatorGLSL.h',
            'compiler/translator/ExtensionGLSL.cpp',
            'compiler/translator/ExtensionGLSL.h',
            'compiler/translator/OutputGLSL.cpp',
            'compiler/translator/OutputGLSL.h',
            'compiler/translator/OutputGLSLBase.cpp',
            'compiler/translator/OutputGLSLBase.h',
            'compiler/translator/TranslatorGLSL.cpp',
            'compiler/translator/TranslatorGLSL.h',
            'compiler/translator/VersionGLSL.cpp',
            'compiler/translator/VersionGLSL.h',
        ],
        'angle_translator_hlsl_sources':
        [
            'compiler/translator/ASTMetadataHLSL.cpp',
            'compiler/translator/ASTMetadataHLSL.h',
            'compiler/translator/blocklayoutHLSL.cpp',
            'compiler/translator/blocklayoutHLSL.h',
            'compiler/translator/BuiltInFunctionEmulatorHLSL.cpp',
            'compiler/translator/BuiltInFunctionEmulatorHLSL.h',
            'compiler/translator/OutputHLSL.cpp',
            'compiler/translator/OutputHLSL.h',
            'compiler/translator/StructureHLSL.cpp',
            'compiler/translator/StructureHLSL.h',
            'compiler/translator/TextureFunctionHLSL.cpp',
            'compiler/translator/TextureFunctionHLSL.h',
            'compiler/translator/ImageFunctionHLSL.cpp',
            'compiler/translator/ImageFunctionHLSL.h',
            'compiler/translator/TranslatorHLSL.cpp',
            'compiler/translator/TranslatorHLSL.h',
            'compiler/translator/UniformHLSL.cpp',
            'compiler/translator/UniformHLSL.h',
            'compiler/translator/UtilsHLSL.cpp',
            'compiler/translator/UtilsHLSL.h',
            'compiler/translator/emulated_builtin_functions_hlsl_autogen.cpp',
            'compiler/translator/tree_ops/AddDefaultReturnStatements.cpp',
            'compiler/translator/tree_ops/AddDefaultReturnStatements.h',
            'compiler/translator/tree_ops/ArrayReturnValueToOutParameter.cpp',
            'compiler/translator/tree_ops/ArrayReturnValueToOutParameter.h',
            'compiler/translator/tree_ops/RemoveDynamicIndexing.cpp',
            'compiler/translator/tree_ops/RemoveDynamicIndexing.h',
            'compiler/translator/tree_ops/RemoveSwitchFallThrough.cpp',
            'compiler/translator/tree_ops/RemoveSwitchFallThrough.h',
            'compiler/translator/tree_ops/RewriteElseBlocks.cpp',
            'compiler/translator/tree_ops/RewriteElseBlocks.h',
            'compiler/translator/tree_ops/SeparateArrayConstructorStatements.cpp',
            'compiler/translator/tree_ops/SeparateArrayConstructorStatements.h',
            'compiler/translator/tree_ops/SeparateArrayInitialization.cpp',
            'compiler/translator/tree_ops/SeparateArrayInitialization.h',
            'compiler/translator/tree_ops/SeparateExpressionsReturningArrays.cpp',
            'compiler/translator/tree_ops/SeparateExpressionsReturningArrays.h',
            'compiler/translator/tree_ops/UnfoldShortCircuitToIf.cpp',
            'compiler/translator/tree_ops/UnfoldShortCircuitToIf.h',
            'compiler/translator/tree_ops/WrapSwitchStatementsInBlocks.cpp',
            'compiler/translator/tree_ops/WrapSwitchStatementsInBlocks.h',
        ],
        'angle_translator_lib_vulkan_sources':
        [
            'compiler/translator/OutputVulkanGLSL.cpp',
            'compiler/translator/OutputVulkanGLSL.h',
            'compiler/translator/TranslatorVulkan.cpp',
            'compiler/translator/TranslatorVulkan.h',
        ],
        'angle_preprocessor_sources':
        [
            'compiler/preprocessor/DiagnosticsBase.cpp',
            'compiler/preprocessor/DiagnosticsBase.h',
            'compiler/preprocessor/DirectiveHandlerBase.cpp',
            'compiler/preprocessor/DirectiveHandlerBase.h',
            'compiler/preprocessor/DirectiveParser.cpp',
            'compiler/preprocessor/DirectiveParser.h',
            'compiler/preprocessor/ExpressionParser.cpp',
            'compiler/preprocessor/ExpressionParser.h',
            'compiler/preprocessor/ExpressionParser.y',
            'compiler/preprocessor/Input.cpp',
            'compiler/preprocessor/Input.h',
            'compiler/preprocessor/Lexer.cpp',
            'compiler/preprocessor/Lexer.h',
            'compiler/preprocessor/Macro.cpp',
            'compiler/preprocessor/Macro.h',
            'compiler/preprocessor/MacroExpander.cpp',
            'compiler/preprocessor/MacroExpander.h',
            'compiler/preprocessor/Preprocessor.cpp',
            'compiler/preprocessor/Preprocessor.h',
            'compiler/preprocessor/SourceLocation.h',
            'compiler/preprocessor/Token.cpp',
            'compiler/preprocessor/Token.h',
            'compiler/preprocessor/Tokenizer.cpp',
            'compiler/preprocessor/Tokenizer.h',
            'compiler/preprocessor/Tokenizer.l',
            'compiler/preprocessor/numeric_lex.h',
        ],
    },
    # Everything below this is duplicated in the GN build. If you change
    # anything also change angle/BUILD.gn
    'targets':
    [
        {
            'target_name': 'preprocessor',
            'type': 'static_library',
            'dependencies': [ 'angle_common' ],
            'includes': [ '../gyp/common_defines.gypi', ],
            'sources': [ '<@(angle_preprocessor_sources)', ],
        },
        {
            'target_name': 'translator',
            'type': 'static_library',
            'dependencies': [ 'preprocessor', 'angle_common' ],
            'includes': [ '../gyp/common_defines.gypi', ],
            'include_dirs':
            [
                '.',
                '../include',
            ],
            'sources':
            [
                '<@(angle_translator_sources)',
            ],
            'msvs_settings':
            {
              'VCLibrarianTool':
              {
                'AdditionalOptions': ['/ignore:4221']
              },
            },
            'conditions':
            [
                ['angle_enable_essl==1',
                {
                    'defines':
                    [
                        'ANGLE_ENABLE_ESSL',
                    ],
                    'direct_dependent_settings':
                    {
                        'defines':
                        [
                            'ANGLE_ENABLE_ESSL',
                        ],
                    },
                    'sources':
                    [
                        '<@(angle_translator_essl_sources)',
                    ],
                }],
                ['angle_enable_glsl==1',
                {
                    'defines':
                    [
                        'ANGLE_ENABLE_GLSL',
                    ],
                    'direct_dependent_settings':
                    {
                        'defines':
                        [
                            'ANGLE_ENABLE_GLSL',
                        ],
                    },
                    'sources':
                    [
                        '<@(angle_translator_glsl_sources)',
                    ],
                }],
                ['angle_enable_hlsl==1',
                {
                    'defines':
                    [
                        'ANGLE_ENABLE_HLSL',
                    ],
                    'direct_dependent_settings':
                    {
                        'defines':
                        [
                            'ANGLE_ENABLE_HLSL',
                        ],
                    },
                    'sources':
                    [
                        '<@(angle_translator_hlsl_sources)',
                    ],
                }],
                ['angle_enable_vulkan==1',
                {
                    'defines':
                    [
                        'ANGLE_ENABLE_VULKAN',
                    ],
                    'direct_dependent_settings':
                    {
                        'defines':
                        [
                            'ANGLE_ENABLE_VULKAN',
                        ],
                    },
                    'sources':
                    [
                        '<@(angle_translator_lib_vulkan_sources)',
                    ],
                }],
            ],
        },
    ],
}
