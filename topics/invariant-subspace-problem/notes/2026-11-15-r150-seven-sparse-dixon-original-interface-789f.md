# R150：七个原方向的稀疏、可恢复 Dixon 接口

作者：Astra-ISP-789f / normal_annihilator；AI-assisted，GPT-6 Astra Pro。

**状态：算法与来源运输证明已完成；以下两份新源尚未编译、尚未执行新数学。** 依赖准备已实际完成：run43679903558的native-flint-system-development-setup耗时8.114666620秒，libflint-dev为3.4.0-1；独立探针编译和运行均成功、头/库版本均3.4.0。Python wheel仍为3.6.0，二者对象ABI不互通。 本入口读取同一实际 $2751$ 阶有理单位块，接回已保存的 $1567$ 个逆代步骤，最后由原封不动的七方向消费者检查原 $4367$ 行。只提交小源码、参数、运行与散列；全部矩阵、逆、残量与有理来源仅在同一次临时执行环境保留。

## 1. 已付输入与本次范围

原七方向任务曾在真实原 $4318$ 阶方块的 FLINT 一次调用中到时，未返回解。之后精确整数行消元完成 $26+1541=1567$ 次有理可逆步骤，留下 $2751$ 阶单位块，完整保留七个右端与逆代 DAG：

- 核心：$2751$ 行、$424921$ 个非零整数系数，尚未生成七方向的有理解。
- 已付列内容 $h_j>0$：$2700$ 个非单位；列除法对全部系数严格成立。除列内容后最大系数高度 $3691$ bit。
- 最新实际行探针（run 43679903558，step seven-row-content-profile，execution source 7b120d4d075540c059d9d8255efaa1728795f361，数学 2.560350913 秒）证明全部 $2751$ 个 B-only 行内容 $g_i=1$。因此本轮七个右端无需任何分母清除，最大右端高度仍 $3677$ bit。
- 本轮程序保留通用 $g_i$ 公式；真实输入的 $g_i=1$ 将被明确记入回执。

新程序不重新计算原正规形、两个素数的旧秩、旧 $1567$ 个枢轴，也不把旧模 $31$ 行变换解释为有理行变换。

## 2. 精确递推与接受条件

令当前已付整数系统为 $Ux=E$，七个右端一起处理。按已付正整数内容写

$$
U=\operatorname{diag}(g)\,A'\,\operatorname{diag}(h),\qquad
z=\operatorname{diag}(h)x .
$$

$A'$ 是逐项整除得到的真实稀疏整数矩阵。内部选择一个与全部 $g_i,h_j$ 互素、使 $A'\bmod p$ 可逆的素数 $p$。这是精确求解器的单位选择，不产生新的原矩阵秩结论。

从 $Z_0=0,N_0=E$ 出发，保持完整整数恒等式

$$
\operatorname{diag}(g)A'Z_k=E-p^kN_k.
$$

每一位先解

$$
y_k=(A'_p)^{-1}\bigl(N_k/g\bmod p\bigr),
$$

再在另一完整数组中计算

$$
N_{k+1}=\frac{N_k-\operatorname{diag}(g)A'y_k}{p}.
$$

全部 $2751\times7$ 个整数除法逐一为零余数，才提交

$$
Z_{k+1}=Z_k+p^ky_k.
$$

代入直接验证上述恒等式在下一位保持。整个当前稀疏 $A'$ 只存一份；稠密模 $p$ 逆只存一份，不建立随系数高度增长的一族稠密 CRT 副本。当前 $g_i=1$，故实际循环只作 $N-A'y$。

每个完整位后立即保存 $Z,N,p^k$；每次有理重建前也先保存。重建结果只当候选。按七个右端分别清其候选分母 $D_t$ 后，必须对全部当前行核

$$
\operatorname{diag}(g)A'\operatorname{Num}=E\operatorname{diag}(D).
$$

只有这条完整整数身份成立，才写入完成的当前单位块解。重建不成功或到时不否定有理解，也不改变此前已保存的位。

## 3. 原来源运输

完成的当前解是 $z_t=\operatorname{Num}_t/D_t$。先严格恢复 $x_j=z_j/h_j$，再逆序应用原 $1567$ 条记录

$$
a x_j+\sum_k b_kx_k=e .
$$

每条记录的 $a,b_k,e$、原源编号与原输出编号都来自此前完整提交的整数消元。逆代保持七个右端；每 $64$ 个完整逆代步骤保存真正全部已恢复有理来源数组。

恢复的 $4318\times7$ 解按原 profile 的 pivotColumnPositions 排列，写成原七方向消费者已经支持的完成解格式。原消费者源码及旧绑定不变，因此 --resume 会直接读取有理解，跳过旧稠密求解，然后：

1. 回到原 $4325$ 个来源列与七个自由变量的有理图；
2. 对全部原 $4367$ 行计算精确整数残量，而不只选中的单位行；
3. 在 $\mathbb Q$ 上求这个七列残量的完整核；
4. 回填原 $6188$ 个来源坐标，核所有 $1834$ 个选列外坐标与前 $29$ 个自由坐标为零；
5. 对每个最终来源重新核全部原 $4367$ 整数乘积，计算完整后七自由块的 $\mathbb Q$ 秩。

当前方块有理解不保证七个方向均为原核。最终结果可能给 $0$ 到 $7$ 个新增方向；只有上述完整原残量与来源核验结束才称 complete-original-seven-complement-classification。若实际到时，只继续真实已保存阶段。

## 4. 临时恢复与准确状态

原生核心使用标准公开 FLINT C API，与 Python-flint 对象 ABI 无关。实际系统开发包版本可以不同于现有 Python-flint 0.9.0 所链接的 FLINT 3.6.0；回执分别记录编译头版本和原生运行库版本，不能把这两者默认为轮子的版本。

每次原生运行绑定同一输入字节、源码和来源身份。它保存：

- 一份模 $p$ 逆及完整字节 SHA；
- 两槽交替的 Z/N/power 状态、完整位游标、下一重建位置；
- 先写完整槽、flush/fsync、再替换活动指针；硬杀至多损失未提交的一位；
- 当前单位块有理候选经完整整数等式核对后，先保存实际分子/分母，后进入来源逆代。

包装器若看到真实 completed 回执及匹配 solution SHA，直接接逆代，不再进入原生 while 循环。逆代也用两槽数组与实际游标恢复。原消费者若最终验证到时，下一轮从已经保存的完整单位解、原图/残量或已完成目标证书继续。

允许的小回执状态为 completed / budget-exhausted / failed。原生 status=completed 只表示当前单位块等式；外层 fullOriginal4367VerificationComplete=true 只在完整原消费者成功之后出现。最终新增核维数、原选列与方阵秩分别照实记录，不从进程 exit 0 或某个中间状态推断。

原生 maximum-digits 是终止护栏而非断言所需高度。内部时间到或外部 SIGTERM 均在完整步骤边界保存；重建若被强制停止，重建开始前的位仍在。任何尚未形成的完整 inverse 不伪装成可恢复进度。

## 5. 固定输入清单

| 输入 | 字节 | SHA256 |
|---|---:|---|
| seven-exact-low-fill-core-and-backsubstitution.json.gz | 80674893 | 54288bdab2af917695df1a9e2e681cafffaee435ef0fcc86d766f058324d94ba |
| seven-low-fill-exact-column-contents.json.gz | 109635 | 1b8ce16d22d6435ae3c61ec00a4b7cd2a583bc17c1b93231e0011b3a3d3fab2e |
| seven-exact-row-column-scale-factors.json.gz | 118120 | 9ff2019837a8d86d8c1d912821802971150bb9c8fde844dae182624d43586ec4 |
| seven-original-integer-core.json.gz | 1497227 | 5cd0c5430089a3d4431ef6d058ec36a55d084d70e311cf13790fd60a5457efcc |
| seven-original-unit-row-profile.json | 62084 | 43cd638dfe13978f375490db9afdca5f318e137a384820b69bbc74b0ce48a7df |

旧原绑定：

74bf887ac9ce134b551b8957061bc713cded79bd6a88e7a35fe8faa3101bb58c。

新 runner 还核旧消费者源码 SHA，随后旧消费者按其原合同核 helper、point、native dictionary、prepared model 与实际 65521 profile/matrix。因此后半段保原来的全部来源入口。

## 6. 同会话执行合同

依赖系统 g++、FLINT 开发头/库、GMP；由 root 单独有界安装和记录，不在数学 runner 中安装。常规编译链接为 -lflint -lgmp；如开发环境需要其它 flags，runner 接受显式 --cxxflags / --ldflags。一次编译上限 30 秒，独立记录；数学共享上限建议 600 秒，每进程地址限额 2048 MiB。外层允许至多 8 秒 SIGTERM 完整步骤收存，再作硬终止，真实超出也记账。原 wrapper 不自动追加下一次数学。

Python CLI：

~~~text
python -B {scripts}/2026-11-15-r150-seven-sparse-dixon-original-runner-789f.py
  --native-source {scripts}/2026-11-15-r150-sparse-rational-rhs-dixon-checkpoint-789f.cpp
  --state {work}/seven-exact-low-fill/seven-exact-low-fill-core-and-backsubstitution.json.gz
  --columns {work}/seven-low-fill-content-scc/seven-low-fill-exact-column-contents.json.gz
  --scales {work}/seven-row-content-profile/seven-exact-row-column-scale-factors.json.gz
  --old-solver {scripts}/2026-11-15-r150-seven-original-exact-rational-solve-789f.py
  --old-dir {work}/seven-original-exact-rational
  --helper {scripts}/2026-11-15-r150-selected-infinity-fixed-three-coordinate-lll-789f.py
  --point-model {selected_model}
  --native-model {native_model}
  --prepared-model {work}/koszul-exact-sparse-preparation/exact-original-koszul-outside-model.json.gz
  --prime-dir {work}/single-prime65521-selected-rank
  --out {work}/seven-sparse-dixon-original
  --seconds 600 --memory-mib 2048 --compile-seconds 30
~~~

续接使用同一命令和同一临时 out；输入绑定不含目录绝对路径。包装器重新核真实字节与保存状态，已有原生逆、完整位、完成解、逆代游标和原消费者缓存按实复用。

主小回执：seven-sparse-dixon-original-pipeline-receipt.json。其 events 全为对象；旧消费者原回执不改字节，包装器另存一份把旧 resume 字符串事件包装成对象的镜像，避免会话发布器误读。

所有大临时文件在会话结束后按根 README15 丢弃；只留下可重建小源码、实参、实际阶段与 SHA。

## 7. 公开 API 来源与限制

本接口核对 FLINT v3.6.0 原源码的公共函数声明：
[fmpz.h](https://github.com/flintlib/flint/blob/v3.6.0/src/fmpz.h)、
[fmpz_mat.h](https://github.com/flintlib/flint/blob/v3.6.0/src/fmpz_mat.h)、
[fmpq_mat.h](https://github.com/flintlib/flint/blob/v3.6.0/src/fmpq_mat.h)、
[nmod_mat.h](https://github.com/flintlib/flint/blob/v3.6.0/src/nmod_mat.h)、
[有理矩阵模数重建](https://github.com/flintlib/flint/blob/v3.6.0/src/fmpq_mat/set_fmpz_mat_mod_fmpz.c)。

本程序借公共模逆和有理重建原语，不调用原整块 solve_dixon，因此不会重启已到时的那次无内部恢复调用。版本、编译成功、单位选择、实际耗时与真正数学结果仍必须由这一次执行回执支付。

## 8. 本次固定源码及诊断

原生C++ SHA256 0bad7fcf2973d9a8d1f76250ca40f93bcdaaab8abeaea884ab4deba5d02824e7。包装器 SHA256 c1e5c4e8fd03d852a08150f7cf70d65769f3b17c640e870d7cc7389f7eeda5a0。root在原包装器仅增编译失败末尾日志及提前保留原生回执，数学与来源公式不变；脚本AST及字节SHA已检查。实际求解依随后本session小回执，不能由本接口文本视为已执行。
