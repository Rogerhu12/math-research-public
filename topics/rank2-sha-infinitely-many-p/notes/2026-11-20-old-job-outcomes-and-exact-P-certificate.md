# 接手后的旧运行结果与 P 完整认证实现

日期：2026-11-20；会话 Astra-rank2-Sha-resume-08eb2b79-20261120。

## 1. 亲读完整旧日志所得事实

以下六个旧任务均已结束，退出码 137，尚无完整末端 PASS。
不能把退出码本身解释为数学反证或已确定的内存耗尽。

| run / job | 最后已确认阶段 | 原日志 SHA-256 |
|---|---|---|
| [43866568746](https://github.com/Rogerhu12/math-research-public/actions/runs/43866568746) / 133296518979 | tate19: actual eta48 U recovery | `ec777ec4e931eacb323e9965ceb07adec2920b062fac71f68b3a2af686b6bf78` |
| [43901392214](https://github.com/Rogerhu12/math-research-public/actions/runs/43901392214) / 133418654415 | persistent PARI basis expansion ready | `75d79d749bb8d5c957fff37ae3f18a17af9f247f2874d449e30217282f47e24c` |
| [43903661921](https://github.com/Rogerhu12/math-research-public/actions/runs/43903661921) / 133426625444 | persistent PARI basis expansion ready | `3db4df27bc53dd7048b1830249cba22a1c3b14576b3f4a7bac2435b0fd310346` |
| [43913500850](https://github.com/Rogerhu12/math-research-public/actions/runs/43913500850) / 133461459569 | r910: single original field inversion start | `96d386d8e57e74a2024e18ef10aead9b893667695e0cc14f160789feece93516` |
| [43922594376](https://github.com/Rogerhu12/math-research-public/actions/runs/43922594376) / 133493496664 | r919: single original field inversion start | `2ac147962b1f204fae1fc0340f6acbc527ce3f6b4aa693166e602ade41f81a97` |
| [43924337986](https://github.com/Rogerhu12/math-research-public/actions/runs/43924337986) / 133499674320 | r919: generic separability certified by specialization | `d2ad2c7da553a514119cb7ed0d111fa2315569faf665ee07cfd6bbf90c8a24b6` |

两条 P 路径分别在 ℓ=1000000033/N=256 和 ℓ=1000003/N=512 完成
全部1226行模素数幂检查、三根合成、有理重建及原初始展开，得到同一坐标 hash
`358238d2595ab4e7873fa41729e725528ab3904cc803d5d1aca22ce010e7be67`。
其后扩展同一 PARI M2 基到4287项，日志确认扩展完成；没有后续完整恒等式回执。
R910/R919 已完成一次关系及两系数的48次模约化，最后停在单个原函数域逆元。
geometry-first 最后仅确认可分特化；不能登记正规化或 RR 完成。

## 2. 同一个 P 末端的等价精确实现

`original_cubic_q_certificate.py` 用
$$
A_N=\mathbb Q[q,a]/(q^N,a^3-17),\qquad N=612(k+1)+3
$$
表示原三次域截断级数。基 $1,a,a^2$ 自由，三条有理多项式全部为零
当且仅当原级数为零。因此它仍逐项认证原 $0\le j\le612(k+1)$ 全窗。
若 $x=\sum x_i a^i,y=\sum y_i a^i$，令
$d_i=x_iy_i$、$e_{ij}=(x_i+x_j)(y_i+y_j)-d_i-d_j$，则完整乘法为
$$
xy=(d_0+17e_{12})+(e_{01}+17d_2)a+(e_{02}+d_1)a^2.
$$
所有乘积在有理多项式 FLINT 后端精确执行并模 $q^N$，不作浮点或模素数替代。
$\theta=q\,d/dq$ 保持理想 $(q^N)$，所以各步截断不损失末端系数。

同一完整 PARI M2 基的高展开逐一匹配全部旧低展开；每个已选乘积的全部旧
低前缀也直接复乘检查。对一组乘积按共同前缀分组，准确使用
$\sum c_{ijk}g_i g_j g_k=\sum_{ij}g_i g_j(\sum_k c_{ijk}g_k)$；
低权的相同公式适用。内层统一清分母后以整数多项式求和，最后准确除回。
因此 A、B 仍是原已重建的两个模形式，不需要存储完整高阶乘积矩阵。

原两项 cusp 支通过 $\operatorname{ord}B=e$、$\operatorname{ord}A=e-1$ 和
$$
y_{-1}=A_{e-1}/B_e=-1,\qquad
y_0=(A_e-y_{-1}B_{e+1})/B_e=-(v_{new}+3)/2
$$
逐项检查，初始13项的原独立检查继续保留。随后原
$$
C=(\theta A)B-A\theta B,\qquad h=qf^3,
\qquad C^3-hA^2(A+v_{new}B)^2B^2=0
$$
在完全相同的 $0..4284$ 范围精确认证。采用
$A^2(A+vB)^2B^2=(A(A+vB)B)^2$ 仅为结合律。
原 u、λ、vnew、全部CM系数、权/维数、三根、全部原有限行和整返回17均未改。

这里已证明的是实现与原认证等价；新运行尚无 PASS，尚不能声明 P 已认证。
后端表示依据 Sage 官方
[有理多项式 FLINT 文档](https://doc.sagemath.org/html/en/reference/polynomial_rings/sage/rings/polynomial/polynomial_rational_flint.html)。
共享文件仅改本题 `.github/workflows/rank2-sha-original-P-small-prime-dixon.yml` 的
依赖/触发清单，确保新 helper 存在；仍只在公开 Actions 做数学执行。

## 3. 真正规化的依赖拆分

第七个旧任务 R922 run43927286602/job133510000884 同样以137结束，
最后确认原eta48可分特化，未到 U 的最终恢复。完整日志hash
`19fc4d5c1e35ffd770568e38e3de55feb902a0b6eaa16d025e3c14b3b1414c04`。
逐行检查旧geometry-first函数可见，它仍先建立原48次域的
$dT/dt$ 及 $a_t=-T/(24t\,dT/dt)$，之后才调用 quotient_divisors；
因此其“最后可分特化”的日志不表示正规化算法已经运行。

新 `produce-original-quotient-geometry-only.py` 直接由同一完整Tate方程
建立同一个24次域 $D=\mathbf F_{29}(s)[L]$，立即调用原
`quotient_divisors`；该函数只读取 D,s,L，逐字保留全部九尖点、
Au、Av、branch、D0和canonical degree的检查。这是可精确验证的依赖拆分，
没有替换几何对象或下游条件。它只报告原商的正规化/除子结果；
U、eta48坐标、完整RR基、两原映射和shadow仍分别需要原有认证。
新本题workflow为 `.github/workflows/rank2-sha-original-quotient-geometry.yml`，
使用同一固定Sage镜像、prime29、原q4500/trace170方程；不保存重算输出。
