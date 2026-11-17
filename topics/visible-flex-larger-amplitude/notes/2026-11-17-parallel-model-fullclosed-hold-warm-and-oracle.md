# 同一准确 Hold 标量与真实 pulse 数据生成的全闭端口初猜

2026-11-17，constructive_model。此条给出一个**已实际生成、可逐字重建的初猜**及其准确标量接口；没有运行非线性求解，没有声称它近等距、浸入、嵌入或满足 reach。它供新的全部角值 Gram 算子使用，不能冒充此前已认证的开放前缀。

## 1. 标量没有换初值

输入仍为 R638/R640/R648 所用的 `parallel-pulse-a5-complete-base.json.gz`，SHA256

`26e53e8cdbdf6205a8bd9b2976cd4bcd36ad8734b0aca69512d705d826c5af72`。

旧标量在每个存储 knot 之间是由**准确 binary 的 a/a′/a″ 三 jet**定义的唯一五次多项式；首 knot 采用原 initial_law 的准确三 jet。新 oracle 以 Fraction 重建这些多项式，并以四次 Bernstein 控制点实际验证旧段 $|a'|<1$。随后沿 R636 的准确 `.99` 初值运输到 `.995`，不是把已打印的浮点 alpha、K 当第二组初值。R636 的原整数三角函数及其已绑定 helper 原样调用。

在 `.995` 后，使用同一 `negative_hold_profile_ivp.py` 已定义的段长及曲率：binary `.002` 从 $K$ 下降到 $-5/2$，binary `.02` 保持 $-5/2$，binary `.02` 上升到 $3/2$，接一段 $3/2$ 平台，再经 binary `.02` 下降到0。以 $S(u)=10u^3-15u^4+6u^5$ 作 ramp，$P(u)=\frac52u^4-3u^5+u^6$ 是其原函数；$\alpha'=-\kappa$，$a'=\sin\alpha$，参考高度导数为 $\cos\alpha$。

若 $\alpha_3$ 为 rise 末角，out 段长为 $h_o$，则

$$
\alpha_4=-\frac\pi2+\frac{(3/2)h_o}{2},\qquad
\ell_p=\frac{\alpha_3-\alpha_4}{3/2}.
$$

故实际末角准确为 $-\pi/2$。记总端点为 $S_*$、准确末半径为 $R$；其后平盘的标量为 $a(s)=R-(s-S_*)$。在接缝有准确 $a'= -1,a''=0$。

## 2. 新的完整积分包围

常曲率段直接用

$$
\int\sin\alpha\,ds=\frac{\cos\alpha_1-\cos\alpha_0}{\kappa},\qquad
\int\cos\alpha\,ds=\frac{\sin\alpha_0-\sin\alpha_1}{\kappa}.
$$

三个 ramp 各固定128个 Simpson panel。对 $f=\sin\alpha$ 或 $\cos\alpha$，可用

$$
\|f^{(4)}\|_\infty\le
K_0^4+3K_1^2+4K_0K_2+6K_0^2K_1+K_3,
$$

其中 $K_j\ge\|\kappa^{(j)}\|_\infty$。源码使用

$$
K_1=\frac{15\Delta}{8h},\quad
K_2=\frac{6\Delta}{h^2},\quad
K_3=\frac{60\Delta}{h^3}.
$$

这些分别来自 $|S'|\le15/8,|S''|\le6,|S'''|\le60$。fall 使用 $K_0=5/2,\Delta=4.653$（已验证 $K<2.153$）；rise 使用 $5/2,4$；out 使用 $3/2,3/2$。单 panel 宽 $d$ 的积分误差逐项加入 $B_4d^5/2880$。partial panel 使用同一公式；查询点自身是时间盒时，另用 $|a'|,|z'|\le1$ 支付半宽。跨段时间盒通过相邻边界值及最大的时间距离统一包围，不选错一侧。全部三角计算及舍入在 R636 的 $10^{-24}$ 整数格上向外进行。

此次实际输出在下列便于阅读的有理外盒内：

$$
2.371299871729814<S_*<2.371299871729837,
$$
$$
0.564734175386577<R<0.564734175387031.
$$

原报告另存完整有理端点、各 ramp 的四导上界和 Simpson 余项。新的 oracle 只包围该同一准确标量；它既不是新的标量初值，也不是完整曲面证书。geometry_amplification 已独立只读核对这些公式与源码，不重复积分。

## 3. 明确的新初猜空间

原819个 $s\in[0,1]$ 的 binary 节点保留。原 M320 的全部保存 $Y,U,A$ 显式截到 M160，保留旋转 $\phi$ 架中的 R-cos、T-sin、Z-cos 三组频率。原 core 的前三个系数保持：

```
0.4619073494154277, -0.05969451246161594, 0.015730056624372334
```

令 $\Theta(\phi)=\phi+\sum_{j=1}^{160}(1-4j^2)c_j\sin(2j\phi)/(2j)$。真实物理 lift 始终使用完整的 $e_r(\Theta)$，**没有截断这个解析函数**。只为选择初猜 q 的有限系数，另在固定8192角点计算 $\cos(\Theta-\phi),\sin(\Theta-\phi)$ 的 DFT 并保留前160模；这个投影的 literal binary 系数一并保存，不把它称作准确连续 Fourier 投影。

在 $s=1$ 后增加104胞：至 hold 末4胞、rise 8胞、至 $S_*-.05$ 的正曲率平台64胞、至 out 起点12胞、out 16胞。因此共有923节点、922胞、1845个节点/真实中点 stage。所有新节点准确写成 $uS_*+v$（$u,v$ 为有理数）；原节点对应 $u=0$。具体分段端点的 binary 段长不改，报告逐项保存这些定义。

在数值 carrier 上，先从真实截频后的 $F(1),F_s(1),F_{ss}(1)$ 作长五次 Hermite 桥至投影圆的三 jet；再在新节点扣除投影版紧支 lift。最终候选定义是

$$
F(s,\phi)=q(s,\phi)+\chi(s)\{[R+S_*-s]e_r(\Theta(\phi))+H e_z\},
$$

其中 q 是保存的**准确 binary 节点三 jet**在上述准确网格上的唯一共享五次场，$\chi=S((s-S_*+w)/w)$ 在外部截为0/1，$w$ 是 binary `.05`。它不被冒称与生成系数时的长物理桥完全相同：lift 有更高径向次数，扣除后再作共享五次本来就是新的场定义。

core 明确按仿射规则设置 $Y_0=\Gamma(c),U_0=e_z,A_{0,Z}=0$；末节点的 q、q_s、q_ss 全部字面0。因此准确端口是

$$
F(S_*,\phi)=R e_r(\Theta)+H e_z,\quad
F_s(S_*,\phi)=-e_r(\Theta),\quad F_{ss}(S_*,\phi)=0.
$$

这可与朝内平盘作 C² 接合，平盘中心使用 Cartesian 图。core 的镜像三 jet 也准确相容。这里只证明了新场的 C² 接缝结构；中间是否浸入、是否自交及真实度量误差仍需读出与求解。

## 4. 实际生成值与投影成本

实际的高度设计值为

$$H=1.9479520470229232,$$

它是保存的原末 Z-mean `0.9780567183886417` 加上准确 Hold 从1至 $S_*$ 的参考高度增量盒中点后所得的 binary 值。**H 是此次真实初猜的自由设计变量，不是已求得曲面的高度**。本次增量准确包含于 `[.9698953286340657,.9698953286344977]`。

数值端点 carrier 为 $S_c=2.3712998717298257,R_c=.5647341753868043$。每个准确 stage 的 a 值都另有有理包围，数值向量首项字面1、末项字面等于同一 $R_c$。此次最大 a carrier 误差不超过 `2.4815220763730974e-13`，最大 stage 时间 carrier 误差不超过 `1.1226466240975015e-14`。这些界仅支付明确的标量/时间近似，**未支付整个曲面求值与数值算子舍入**。

保存节点上被 M160 截掉的系数 l1 最大值按 Y/U/A 分别为

```
9.047886699421574e-7, .0010815668872330541, .8681159817010814.
```

这是普通浮点系数诊断，不是连续余项证书。core 若干 T 系数为满足准确乘法关系而显式调整，最大 `1.734723475976807e-18`；U0 与 A0_Z 原已准确满足。其他818个原节点的保留三 jet 全部逐字保留。末 q 三 jet 置0前的最大浮点差依次为 `5.1071e-15/1.6210e-14/3.8022e-14`，该置零属于新候选定义。有限圆投影在自身8192网格的误差约 `5.7583e-14`，不代替解析 lift。

需要特别区分：原 pulse 与此 Hold 标量在 `.995` 后不同。因此即使没有 M160 截频，这段原 pulse 场也仅是 Hold 问题的初猜；R648/R651 等原开放场认证没有搬给此新场。

## 5. 冻结身份和实际重建

新源：

- `parallel-model-full-hold-oracle.py`，11694 B，SHA256 `a1ed8fa5d2186f400ea50a1d609574ec6996e59317a57638a6820a59cf0e7670`。
- `parallel-model-fullclosed-hold-warm.py`，11230 B，SHA256 `bee5ae587bd519189b0b27c249987d80d82ab66822cd4f1ea4746a769f7fb3c3`。

已刊依赖：R636 integer oracle `babd589d07c91d8067f9ef2011ae53712aaf6dbdbe22bed25c29116771b237a0`（它自己检查 helper `e480a2ca7ebd5911768cad04ef7b98319ff2cff1840cf71531eaf2b574b4211a`）；同一 Hold 源 `ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1`。原26e53输入沿已刊完整 pulse 前缀生成配方重建，raw 不入库。

实际输出均留仓库外：

- `parallel-model-fullclosed-hold-warm.npz`，8767021 B，SHA256 `401255b7328ba2e4cdfe5af94d0a0896859960f1b474961d30aff33d8248f02a`。
- `parallel-model-fullclosed-hold-warm.json`，554070 B，SHA256 `0c499334cebe74f0c417ccb89b5ee4dcf86cb07dfbab1f0d46c0b805f4a71b80`。

npz 提供 `mesh,qjets,a_stages,radius,Hcap,width,fixed_core_first3,circle_projection,a_stage_absolute_error,stage_time_absolute_error`；qjets shape `(923,3,482)`。该空间 free size 为1,332,245，不形成稠密 Jacobian。生成耗时4.92秒，没有运行 Gram 全域扫描或非线性求解。

将两个新源放在仓库外 `$WORK` 后，可运行：

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python "$WORK/parallel-model-fullclosed-hold-warm.py" \
 --input "$WORK/parallel-pulse-a5-complete-base.json.gz" \
 --scalar-source "$WORK/parallel-model-full-hold-oracle.py" \
 --integer-source "$TOPIC/notes/2026-11-17-parallel-inward-integral-enclosure.py" \
 --hold-source "$TOPIC/scripts/parallel_20261117_negative_hold_profile_ivp.py" \
 --out "$WORK/parallel-model-fullclosed-hold-warm.json"
```

计时和路径字段及 npz 容器元数据可改变文件 SHA；保存的 binary 系数、准确节点定义、标量盒及 source/input 身份是重建对象。独立角值 Gram 算子接收该 bundle 后的实际读出另记；本条不预报其结果。
