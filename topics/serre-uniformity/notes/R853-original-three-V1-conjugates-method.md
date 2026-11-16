# R853：三个原 V1 共轭与真实函数域下降入口

日期：2026-11-16。状态：执行契约；新算术只在公开 Actions。本首 scope 不构造完整272列 involution、一般 $\Gamma$、RR 空间或任何高度。

## 1. 原目标与准确来源

使用 [原 R802 半线性作用](../results/R802-original-semilinear-parity-and-degree-seven-relations.md) 及 [有限 RR 来源桥 §6](2026-11-16-original-Y-finite-RR-matrices-and-source-leaves.md)。原 $K=\mathbf Q(s)$、$s^2=-3$，$c_0$ 固定 $\xi=\zeta_{41}$，原算术共轭满足

$$
[q_Y^n]\varepsilon(c_YF)=(-1)^n c_0([q_Y^n]\varepsilon(F)).
$$

固定三个实际目标

$$
\tau=e_0,\qquad\sigma=e_1+e_{73},\qquad w_0=e_2.
$$

$e_i$ 是原 R786 整尺度 $82^2=6724$ 的 V1 基。原 R806 真实 configuration 中的 `original_tau_index=0`、`actual_sigma_integer_n=1`、成功 primitive definition 的 `index=2` 固定这三个对象；不猜另一个候选。

原 R786 的146个 `R786-exact-power-1-row-####.json.gz` 已各保存129项、每项40个整数系数。本次只读前14项，构成

$$
A_{40n+r,i}=[q_Y^n\xi^r]e_i,
\qquad A\in\operatorname{Mat}_{560\times146}(\mathbf Z),
\quad 0\le n<14,\quad 0\le r<40.
\tag{853.1}
$$

完整14项在原 V1 上单射，因为二十 cusp 的总零阶 $20\cdot14>272$。实际 R837 reflection 已给同一个 $A$ 的146个选行 $I$、全部146列，以及非零模 minor。只复用这个已成选行证书；不重算原 rank、模 inverse 或反射后的 P0 值，也不把这些编号换到280行的实坐标矩阵。

## 2. 唯一新 solve 与完整终验

令 $V$ 的三列分别为原 $e_0,e_1+e_{73},e_2$ 的146维坐标，令 $S$ 是对第 $40n+r$ 行乘 $(-1)^n$ 的对角矩阵。全部原 Fourier 系数是 $\mathbf Z$ 中的 $\xi$ 坐标，$c_0$ 固定它们；三个目标的系数也在 $\mathbf Q$。因此新右端是

$$
B=SAV,\qquad C=A_I^{-1}B_I\in\operatorname{Mat}_{146\times3}(\mathbf Q).
\tag{853.2}
$$

只做这个三右端准确 solve，并完整验证

$$
AC=B
\tag{853.3}
$$

的全部 $560\times3$ 原坐标。通过后，由 V1 单射和原共轭保持 V1，$C$ 的三个列向量就准确等于 $c_Y\tau,c_Y\sigma,c_Yw_0$。也保存 $SAC=AV$ 的完整核验，明确二次原半线性作用回到这三个原目标。没有重新生成146条旧 Fourier 系数。

准确分数直接按 `[numerator,denominator]` 保存，不作模重构猜测。旧选行只证明 (853.2) 的合法性；成功结论仍包含完整 (853.3)。不计算新 $146\times146$ 共轭表。

## 3. 原 normal 表达与函数域作用

R805 的 degree1 normal 基为 $\beta_{i-1}=e_i/\tau$，$2\le i\le145$；因原 $\sigma=e_1+e_{73}$，

$$
e_1/\tau=z-\beta_{72},\qquad z=\sigma/\tau.
\tag{853.4}
$$

对一个新列 $c=(c_0,\ldots,c_{145})$，其截面除以原 $\tau$ 的准确 normal 表达为

$$
c_0+c_1z+\sum_{i=2}^{145}c_i\beta_{i-1}-c_1\beta_{72}.
\tag{853.5}
$$

这是固定原基定义的线性运输，不是另求乘法。核心逐项重建原146个 V1 系数，核它恰回到 $c$；保存原 R806 的 R805 free-basis spec，不能改 basis label。

令三式 (853.5) 分别为 $T_c,S_c,W_c$。输出准确有理函数 DAG

$$
c_Y(z)=S_c/T_c,\qquad c_Y(w)=W_c/T_c,
\qquad c_Y(s)=-s,
\tag{853.6}
$$

其中 $w=w_0/\tau$。$T_c\ne0$ 来自准确原 $c_Y\tau\ne0$；不作近似零判。原 R806 已证 $K(Y)=K(z,w)$，故 (853.6) 定义整个原函数域上的真实半线性作用。输出保原 R802 的扭曲，不把对 normal 系数的单独共轭当成算术作用。

为使 (853.6) 的函数域来源完整，DAG 同时保存原 $W$ index、其34组原坐标的 file/bytes/SHA 和原 cyclic witness 引用。令 $K_w=(e_0,We_0,\ldots,W^{271}e_0)$，分别给三个 (853.5) 向量 $v_c$ 定义准确节点 $K_w u_c=v_c$，再用 $\sum_{i=0}^{271}(u_c)_i w^i$ 表示该原函数。这是原非零 cyclic 子式保证合法的 unit-solve 表达；本次不执行这三个 $K(z)$ solve，不读取或重算34组 W 数值，更不形成大逆。未来对有限 RR 核的实际作用按消费者需要执行。

## 4. 最小源闭包与 CLI

核心文件 `scripts/R853_original_semilinear_V1_conjugates.py`，CLI：

```text
--config expanded-job.json --out output --budget-minutes 300
```

`expanded-job.json` 固定 `result/core/core_sha256/p=41`、本方法及三证明的路径与 SHA，并有 `sources` 三组。每组含原 BASE 身份、`directory`、完整所选 `files` 的 file/bytes/SHA、`selected_files_sha256`、原 certificate、stage manifest 与 configuration SHA。绝对目录和运行预算不进入数学 tag。

| 原 source | 必需数学成员 |
|---|---|
| R786 | 全146个 power1原行，原 cert/stage manifest/完整 manifest 和原 source/run/core 元数据 |
| R837 | 原 `R837-original-V1-reflection-minor.json.gz` 及其 `successful_attempt`；原 cert/stage manifest/元数据 |
| R806 | 原 accepted candidate、对应 definition、polynomial-multiplier index；原 cert/stage manifest/元数据 |

R806 的34组 W 坐标不选入；R837 的其它积、P0/V2值和1213矩阵不选入。本 core 用实际来源字段核 τ、σ、w0 与原 free-basis，而不是重作这些数学结论。

原 R786 producer 是 run `43682100611` / source `dd262672a8b1e2af82277b15e0fa766038609670`；原 R837 为 run `43770995901` / source `fa17c77fe36fddd9df06677569984d1ea71a6b41`；原 R806 为 run `43707290840` / source `75b1d56c821abe34660477ba8b4c7f7b75a4382b`。实际 raw 元数据在本次 IO 闭包中逐字保留。新的 source SHA、tag、run 与输出都使用 R853 自己的真实身份。

## 5. 原子阶段、续接与成功含义

数学 RESULT 为 `R853-original-semilinear-V1-generator-conjugates`，FINAL 为 `p41-original-semilinear-V1-conjugates-certificate.json`。

新阶段统一 `R853-*.json.gz`：原源与已成选行 audit、三准确坐标及全560终验、三个 normal 表达和函数域作用 DAG。已成阶段原子写入并保完整 configuration；续接直接回用，不重 solve。只有三个坐标和 DAG 都完成时 FINAL 才 `complete=true`。预算或硬中断保已成阶段；`core-receipt.json` 明确实际结果和停因。

stage manifest 只列实际完整数学阶段，排除它自身。所有成功输出保原尺度、三目标顺序、旧选行、完整验证范围与各 source refs。

成功仅给三个真实共轭、其 normal 表达和准确函数域下降入口。完整272 involution、R813 的 $g,h$、一般 $\Gamma$、128维 RR 核、$a_j$、$\alpha_0$ 和原高度都不在本次新计算范围。
