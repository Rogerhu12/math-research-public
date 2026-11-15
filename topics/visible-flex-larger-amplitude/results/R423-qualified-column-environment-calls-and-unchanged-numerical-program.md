# R423：recorded operator 三处环境调用的限定名字解析与原数值程序范围

作者：ChatGPT（AI，amplitude 分工）。2026-11-15。结论类型：原源码名字解析的确定工程修复及条件程序等价；没有本地编译或科学计算，没有把修复预称为完整阶段成功。

## 1. 原始证据与本结论的对象

actual190 原完整结果见 [R403](R403-actual190-persistent128-acceptance-stage-compile-block-and-partial-audit.md)。其 owner 在当前128状态接受一步并完成独立 replay，但 stage 编译返回1，完整576乘224变分尚未开始。原编译错误明确指出 `column_environment` 的不明确调用，并随后报告 `em`／`e1` 未声明。这与如下原文件的实际声明和调用直接对应，不是由 job 状态推测数值失败。

冻结文件为 `computations/geometry_20261115_native_preassembled_operator_trace128.hpp`，24706字节，SHA256 `b16fac2b38cc873da63a759f505fde7ccf5b3b6fd9bd0f709647b65be78a7dc8`。它在 `preassembled_trace128` 内声明：

```cpp
using StepDirections=hoisted_trace128::StepDirections;
// ...
static EnvironmentDirection column_environment(const StepDirections *parameters,
    int field,int column,int columns){
  return hoisted_trace128::column_environment(parameters,field,column,columns);
}
```

而同一文件的 `rk4_batch_parameters` 以未限定名写三处：

```cpp
const auto e0=column_environment(parameters,0,col,state.columns),
  em=column_environment(parameters,1,col,state.columns),
  e1=column_environment(parameters,2,col,state.columns);
```

这里换行只为展示；待发布新正文保留原行排版，唯一变化是三处调用名增加 `preassembled_trace128::`。

## 2. 不明确性的完整原因

类型别名 `StepDirections` 不创建新的 C++ 类。参数 `parameters` 的静态类型仍为指向 `hoisted_trace128::StepDirections` 的指针，相关的名字查找可包含其原命名空间。因此未限定函数调用既有普通查找得到的 `preassembled_trace128::column_environment`，又可经参数相关查找得到 `hoisted_trace128::column_environment`。

两个函数在这一调用的四个参数上都可作相同等级的匹配。原本地 wrapper 的作用是明确委托后一函数，不使两个声明在未限定调用的重载集中自动合并。即使运行时 `parameters==nullptr`，也不改变其静态类型及源码名字查找。

此处是普通非模板函数体的编译。后来 SIMD 内核即使不调用这个旧 RK 函数，也必须成功解析被 include 的函数体；不能由“新路径只用新 RK”推断旧歧义不会阻断编译。actual190 的真实首错是本结论的实际证据；其 `em`／`e1` 后续错误与前面的联合声明未能形成一致，并不提供新的数学失败证据。

## 3. 独立最小补丁

新独立文件为 `computations/geometry_20261115_native_preassembled_namespace_qualified_trace128.hpp`，24775字节，SHA256 `f82cd9504fc7396664941a76e687abd489aae8766482977c80a675c9e9a9b9ae`。三个准确替换为：

| 原调用 | 新限定调用 |
|---|---|
| `column_environment(parameters,0,col,state.columns)` | `preassembled_trace128::column_environment(parameters,0,col,state.columns)` |
| `column_environment(parameters,1,col,state.columns)` | `preassembled_trace128::column_environment(parameters,1,col,state.columns)` |
| `column_environment(parameters,2,col,state.columns)` | `preassembled_trace128::column_environment(parameters,2,col,state.columns)` |

每个原调用在冻结正文恰出现一次。新正文把这三项按顺序逆换后，全部24706字节恢复为原 `b16fac2b...` 文件。没有更改声明、参数、返回表达式、算术括号、常数、循环、顺序、异常分支或检查。

限定的 `preassembled_trace128::column_environment` 准确选中上述本地 wrapper；其原函数体已经用限定名调用 `hoisted_trace128::column_environment`。这既消除外层的参数相关候选歧义，也保留设计中的委托链。

## 4. 条件程序等价的准确含义

**命题。** 对任意满足原接口的输入，如果所比较的基准是“这三处本来显式调用原 `preassembled_trace128` wrapper”的程序，则补丁与该基准调用同一函数体、传相同参数，之后执行相同的环境选择和数值表达式。补丁本身不改变 binary128、整数digit、SIMD、root、RK或残差的算术图。

**证明。** 三处新增的限定符只作用于名字解析。被选中的 wrapper 未变；每次实际传入的 `parameters`、常数字段0／1／2、`col`、`state.columns` 未变。wrapper 的唯一返回表达式仍是对原 `hoisted_trace128` 函数的同参委托。三调用以外的全部字节通过逆变换完全恢复，故其前后循环、求值表达式与异常分支亦保持。证毕。

这个命题不声称一个编译失败的旧实际 executable 已产生可逐词比较的输出；actual190 没有该 stage executable 的科学结果。也不声称新编译必然通过所有其他位置，或新运行必然在8000秒完成全部阶段。真正的编译状态、运行范围、backend和全部最终消费者必须由新公开 Actions 给出。

## 5. 与192／196源码及后继199的关系

冻结192和196均以 `b16fac2b...` 作为 `RECORDED_HEADER`，把它复制进实际 stage 编译目录；它们的独立数学 header 都 include 这个 basename。因而源码具有同一解析风险。[actual192／R406](R406-actual192-persistent128-return-and-request-number-readback-block.md) 已返回 `stage=false`，但其 stage 内部具体编译原因未返回；不能由这里的静态风险补填成 ADL 故障。本文定稿时196仍待实际终态。本结论不修改任一原运行源码或请求。

独立199沿完整196入口，旧84个 source pin逐值保留。其原 SIMD数学 header、stage C++、R405完整digit kernel、R414 SIMD kernel及所有原数学组件直接复用原字节。新 compiled include 视图只把本独立修复后的 header 正文写到原 include 所需 basename：必须同时记录旧 baseline 身份、新独立文件身份、实际临时编译文件身份及三处完整逆变换。这个重命名是明确临时source视图，不是声称实际执行的字节仍等于旧 `b16`。

新的 launcher/helper/bridge/necessary reader只绑定该来源与独立运行身份；它们仍执行真实旧91输入恢复、fresh64完整J／R273、持久128 owner、全576乘224 stage、112 boundary、mixed338乘112 endpoint及独立audit。原所有数量、科学预算、root与native阈值不变。新头文件能解析不是新的科学接受门。

## 6. 未扩大数值和数学结论

[R402](R402-recorded-literal-block-operator-equivalence-and-rounding-scope.md) 的准确实对象仍固定实际记录的 literal sine／cosine／Gram及名义因子；名义因子乘积不被假定等于原矩阵 C。R405／R414 对完整有限word的dot和SIMD整数partial的条件证明仍是原证明。本名字补丁不支付整体变分误差、C与真实根导数差、重结合误差或连续ODE误差。

所有113个有效位、真实指数跨度、完整wide fallback、次正规直接RN、符号、实际CPU选择及scalar fallback都不修改；不删任何stage、列或行。原完整 C方向残差、两回代、原finite检查、完整226状态、两mean、原root branch与RHS/RK、所有最终输出范围继续公开负责。

必要读回仍为一份≤90000字节的原字段结论，真实科学退出与协议退出分开。完整大矩阵只在本次Actions临时目录，原字段选择和身份不能被描述为root逐值读取整个大树。只有必要读回成功且所有owned child静止后才清理；本修复不创建可持久的已接受场锚。

本文与补丁仅以原源码文本、字节身份及实际190错误记录为依据，没有本地编译、导入、科学运算、对拍或微基准。实际199结果另记R424。
