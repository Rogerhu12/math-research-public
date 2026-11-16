# R535：原128 root局部有限字词与真实compiler接线接口

作者：ChatGPT /root（AI），2026-11-16 UTC。完整证明见[R535](../results/R535-original128-local-finite-root-words-and-real-compiler-hook.md)。

## 1. 已完成与尚未注册

本项提供可由公开Actions直接使用的header、完整literal source plan和Python源准备/真实compiler安装API。它们不启动新的科学owner、不作benchmark或fixture，也未修改冻结221/225。拟request226/R536入口/R537实际仅为协调保留，未派发。

严格保留原6000秒owner、1200秒replay预留、19200秒原全钟及四后置组件原caps。任何source preparation或真实compile耗时都由原调用者按其既有阶段计入；安装函数不创建新clock或额外科学allowance。原32×10 native、30×20 root、M112/N2048/576段/577×224、226输出及双mean、全部原域/BC/RMS/FD/fullDN/fresh replay/final audit不减。

R535针对R509的先行owner重复计算；R532/R534后置同DN模型另立真实来源，不在本接口中暗接。原225的R522/R515后置优化可由未来226完整入口正常继承，不改其算法。

## 2. 文件身份

| 正式文件 | bytes | SHA256 |
|---|---:|---|
| computations/root_20261116_native_root_finite_words.hpp | 7102 | 6706eae670bf5746eb42d194bd456d290c290d451ddc52d80359d0263f90e7cc |
| computations/root_20261116_native_root_finite_words.py | 10892 | 1c99623e2cd63d0a4700011c96e5054645cf7dd8ee5cf3357f0c77d1727026db |
| notes/R535-native-root-finite-words-complete-source-plan.json | 10232 | f3b7900f0e670441404c707dce2144241ee9b72581c5999dd8ce95b91764607b |
| results/R535-original128-local-finite-root-words-and-real-compiler-hook.md | 17788 | 564379516762900d03ea7b743905bbf113f45286ca6a1df1deb0f0562f42bcd3 |

接口自身身份由外部publication metadata登记，无自引用。两份生成CPP只作本次工作目录的include依赖，不收入Git或另作旧standalone请求入口：

- root_20261116_native_root_finite_words_primal128.cpp：25230 B / 3e1cb0a416418fe56fbee889df5debdfc9ed097b797a1b8e086b563ce4fd9241；
- root_20261116_native_root_finite_words_trace128.cpp：34950 B / 2e122e0ca6ad21e1c11ab711cc5af40a6955d3ff054f6cd445dbd885fbb98b12。

临时declared compile_owner函数原3860 B / be019045058f4616f98b07e19c0d8d3901e979ce2b1ba7d4259c65fcae4ae46d，改后5206 B / 2d8754983d9e9f2fae9b1f5695840fd180d83fa996796818dc4462684c5dc55c。函数源在实际公开Actions的原owner namespace内执行；此处只做文本核对，没有本地import/AST/compile。

## 3. 必备原源与实际HERE

adapter的HERE必须是真正公开checkout内本课题computations目录。必须保留四份原源：

| basename | bytes | SHA256 |
|---|---:|---|
| geometry_20261115_native_primal128.cpp | 23890 | 1b59cd1059c147f3fedf28a663fed25049c80a42d782838506aba4a7b7df591d |
| geometry_20261115_native_trace_variation128.cpp | 34622 | 8c40b4c7ed214a16afd06cd0157bf861822cb217a72bd0117bbed7f2c954204d |
| geometry_20261115_native_persistent128.cpp | 22364 | 7789007e4213af539146353ac48bbedc2d8e611e3fb76538d2a96b616643f7fd |
| geometry_20261115_native_persistent128.py | 43371 | 767a4c4b329779fd200e6ec6f674ab62db9f6a65984628299d1f2241f83dd322 |

其余原packet launcher、bridge、R273、captured-band等PINS与所有原完整输入来源也必须由未来完整request保留。本模块不以这四项冒全部336或356来源闭包。

所有新view在真实HERE以新basename生成；原四文件从不覆盖。已有同名新view只在完整bytes/SHA相同才复用；不同内容不覆写成“通过”。新header和source plan均是正式小源，所有科学raw仍由原owned临时树保存，不能写入Git/Release/artifact。

## 4. 原源准备阶段调用

推荐实际API：

~~~python
binding = root_words.prepare_sources(
    HERE.parent / "notes" / "R535-native-root-finite-words-complete-source-plan.json"
)
~~~

root_words必须通过原source closure绑定并加载实际adapter，不是一个同名任意对象。adapter内部固定完整plan bytes/SHA；每个base、header、output均核实际文件。返回BINDING_SCHEMA：

~~~text
R535-native-root-finite-words-source-binding-v1
~~~

完整binding包括实际source_root、adapter、plan、header、四原来源、两个生成来源、每view literal数量与完整逆源恢复标志，并明确：

~~~json
{
  "source_preparation_complete": true,
  "compiler_completed": false,
  "scientific_evaluation_performed_by_preparation": false,
  "no_original_source_file_overwritten": true
}
~~~

这些只是该次真实源准备记录。实际compiler尚未执行，不能填tol、replay或新的accepted字段。

独立CLI只形成相同source binding，供原workflow源准备step使用：

~~~text
python3 computations/root_20261116_native_root_finite_words.py
  --source-plan notes/R535-native-root-finite-words-complete-source-plan.json
  --binding-out <本次实际owned临时source-binding文件>
~~~

上面路径相对课题目录，调用者须用真实绝对路径或该准确cwd。binding-out以xb新写，返回一份原canonical+LF且小于90000 B的source准备记录。它不是科学必要正文，也不能代替之后的原科学reader/quiet。

## 5. 唯一真实owner接点

原225 same-call owner真实顺序包括：

~~~python
changed = build_view()
exec(compile(changed, str(HERE/VIEW_PLAN["baseline_file"]), "exec"), scope)
owner_scope = scope["source_scope"]("owner")
# 随后原参数设置及 owner_scope["main"]()
~~~

未来新caller应在该真实owner_scope形成后、main前加入：

~~~python
installation = root_words.install_owner_compiler(owner_scope, binding)
~~~

它必须使用同一份实际准备的binding，并把installation放入本次实际调用元数据。不能生成另一个未被main消费的scope或只更换SHA表。

安装API：

- 要求GITHUB_ACTIONS=true且GITHUB_REPOSITORY为公开Rogerhu12/math-research-public；
- 要求原main和compile_owner的__globals__都是该同一实际dict；
- 要求原CPP/ORIGINAL_CPP/TRACE_CPP字面及原祖先pins正确；
- 核所有实际新source/header、原来源及adapter/plan的完整身份；
- 从完整原owner文件抽取唯一原compile_owner，按4个literal形成完整新函数并核逆源；
- 保全部原PINS，新增新header、两view和adapter；
- 修改真实compiler所读的ORIGINAL_CPP/TRACE_CPP为两个新basename；
- 在同一owner_scope定义新compile_owner，原main/solve/replay不重写。

返回安装schema是BINDING_SCHEMA加-installed-v1，明确actual_compile_not_yet_called=true。同scope重复安装报来源错误，不捕获后改跑旧binary。每次真实call有其原fresh owner_scope；固定source view可跨call按完整身份复用，数值缓存始终只在一个C++ root局部对象内。

## 6. 实际编译与原语义

原persistent CPP保持7789007e全文。它包含的native_frozen_trace_variation128.inc由原owned-work生成，里面是新trace prefix加原full226 observer。兼容basename保留，不再声称whole prefix frozen。

新trace prefix实际include新primal，后者实际include新header。原完整evaluate函数的数值体原字不变，原四个observer改动及原逆替换保留，所有576×226 stage输出完整形成。

真正g++仍由原compile_owner调用一次，原参数：

~~~text
-std=gnu++17 -O3 -fopenmp -frounding-math -ffp-contract=off -fno-fast-math
~~~

原300秒compile allowance、同process group、stderr/stdout日志、原terminate_owned、实际exit与executable检查保。原outer owned registry、deadline/quiet由完整调用者继续负责，本模块没有新owner子进程或守护线程。

实际成功回执：

~~~text
compilation.root_finite_word_cache_compilation_source_binding
~~~

其中compiler_completed=true只在g++真实exit0及executable存在后产生，连同完整command、include/header、adapter/plan、actual views、祖先、stdout/stderr/executable身份返回。原frozen_R283_numerical_prefix_is_byte_identical和only_frozen_trace_standalone_main_excluded明确false；真正数学变化只有论文与plan声明的局部词共享，不能再返回旧whole-source不变旗。

若prepare、install或compile失败，原完整错误按实际阶段保留，不能伪造compiler_completed或清除原raw。新回执缺失不是新方法数学失败；来源错误与资源partial分别记。

## 7. 新统计的完整消费合同

原owner每个实际evaluation内的root_statistics.root_finite_word_cache是真实新对象。完整字段在R535§535.8，包含18个计数、last_present与完整last以及固定scope说明。未来必要reader必须按真实所属event/call/iteration/trial/evaluation key保全部对象，允许具名表组织但不得丢字段、last或缺键区别。

原RootStats字段不被新统计替换。新计数不参与原tol/strict decrease/域判断；不能以fixed_qualified_builds>0推断所有原stage完成。固定/U的builds_completed包括资格决策fallback，不代表完整科学角域；U row计数在原D/S/A检查之前增加。

last.phase、mode_zero_based、angle_zero_based及fixed_words_used_in_evaluation/u_words_used_in_evaluation按实际状态保。原stage顺序合并与线程完成墙钟不同；不称其为整个进程的最终时间事件。未形成记录时保last_present=false/last=null，不能用零地址补齐。

当前225旧necessary reader的evaluation选择不包含root_statistics，本项不假装已经读回新字段。R536须在真实新reader加入完整新具名对象及actual compiler binding；正常/失败/recovery共用真实消费点。原单正文90K/70不改；实际仍超限就保原partial，不通过裁字段让它“通过”。

## 8. 数学保证与未付实际结果

R535完整证明给出同一finite输入和原Q运算语义下：

- 同root的momentum/pt/P/Pt字词相同，全部原角点/模式与累加序不变；
- 同evaluation的U模式系数字词相同，所有原u_j*sn及U累加仍发生；
- 原全部Angular/residual/域、root选择、RHS/RK与完整native试步有限词按原顺序保持；
- 原fallback与新finite资格分责，所有非finite资格只使本项退回原完整表达式。

完整构建可能先计算原早拒路径未到的角点，资格扫描、分配、复制和计数都有成本；不保证墙钟、资源前沿、NaN payload或fenv sticky flags相同，不保证任何实际速度、rank、convergence、tol或末门通过。

拟226须从原完整真实输入重做，不能迁已清221父。当前R535尚无新request/source-run身份、编译成功、计数值、残差、耗时、fresh replay或后置结果。实际结果由R537唯一原日志读回再刊，始终继续open与README原目标。
