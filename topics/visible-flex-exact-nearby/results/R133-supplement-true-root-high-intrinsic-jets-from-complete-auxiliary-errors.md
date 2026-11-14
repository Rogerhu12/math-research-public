# R133 续篇：真实根的十二列原始径向导数与完整高阶 intrinsic jets

2026-11-14，visible-exact / phase_inverse。

**解析合同已证明；新增真实根高阶数值列仍须公开 Actions 实际执行。**
本篇只增加原同一标量 germ 在真正根区间上的高阶导数。
它不重跑已经完成的两个辅助复域，不把原有限三阶证书当高阶证书，
也不改变物理背景、参数、根、Fourier 方向或任何接缝。

准确依赖是
[原辅助解析延拓与完整复三阶](R133-supplement-auxiliary-root-piece-analytic-extension-and-complete-complex-third-jets.md)、
[原辅助域公开执行](https://github.com/Rogerhu12/math-research-public/actions/runs/43640181602)、
[根 Taylor 递推](R133-supplement-exact-first-Airy-root-jets-and-Taylor-tail-derivatives.md)
及原 `fourfold_codazzi_cubic_target_jets.py`。
下面把“新算的有限列”与“复用的完整无穷余项”逐项分开。

## 1. 同一个根与两个已经完成的解析误差域

保原 exact-affine 对象 SHA256
`91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848`、
原真实根 germ SHA256
`397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864`，
及原固定 intrinsic 参数 $\eta_0$。有限求值仍保留原半宽
$10^{-9}$ 的输入盒作更宽包络；它不授予其它 intrinsic 参数
同一个根区间。本文所有真根恒等式只用于原固定 $\eta_0$。根满足
$$
 r_*\in I_*=
 \left[
 \frac{1191984371497}{5000000000000},
 \frac{2383968743003}{10000000000000}
 \right].
 \tag{H.1}
$$
原 scalar germ、512 个原 primitive 节点、原 20 次标量多项式
及其两个 NPZ 字节完全不变。此处紧支参数 bump 恒为零，
因此这些 intrinsic jets 同时适用于原实或复 $|\delta|\le10^{-8}$ 族：
这只是原度量在该根 germ 上对该参数的准确独立性，
不是把未知 PDE 解或其它物理 piece 外插到该盘。

原公开 run `43640181602` 的 native
`6276b4b8bd117b3092ce633b7164ff99968100f10b09cbaef8850d4c03f6b24f`
已经分别完成
$$
 R_1=10^{-4},\qquad R_2=5\cdot10^{-4},\qquad
 \mathcal Q_i=\{\operatorname{Re}r\in[I_*^- -R_i,I_*^+ +R_i],
                         \ |\operatorname{Im}r|\le R_i\}.
 \tag{H.2}
$$
只消费这两个 `complete=true, proved=true` 的 case。
原另外两个失败 case 和原 process 的 return1 保留，
不能把整个原作业重新标成成功。

令 $F$ 为原完整初始 immersion 在原旋转三坐标中的表示，
$F_N$ 为同一原有限 primitive 规则给出的有限 Fourier 多项式。
它包括原 FFT 频率、Nyquist 项准确置零、原 parity 对称和两个
准确零 primitive mean；物理半径及高度 mean 另按原定义加入。
每个 $r$ 上有限规则是一个确定全纯函数。新的 interval FFT
只包围它的导数，不另选 Fourier 近似。

每个已成 case 保存的
`complete_primitive_radial_errors[k]`，$0\le k\le5$，满足
$$
 \max_{\alpha=1,2,3}
 \|\partial_r^k(F-F_N)_\alpha(r,\cdot)\|_{A^0}
 \le \epsilon_{i,k},\qquad r\in\mathcal Q_i .
 \tag{H.3}
$$
这些是原无限 Fourier 余项费用，有限运算舍入另在点值 balls 中。
不是用“有限 Fourier 尾看起来小”代替 (H.3)。

## 2. 已成完整误差的高阶 Cauchy 延伸

对原固定 $\eta_0$ 的真实根 $r_*\in I_*$，闭圆盘 $|r-r_*|\le R_i$
都包含在 $\mathcal Q_i$。固定原 $\eta_0$，对
$\partial_r^k(F-F_N)$ 作 Banach 值 Cauchy，得到
$$
 e_j=
 \min_{\substack{i=1,2\\0\le k\le\min(j,5)}}
       \frac{(j-k)!\,\epsilon_{i,k}}{R_i^{\,j-k}},
 \qquad
 \max_\alpha\|\partial_r^j(F-F_N)_\alpha(r_*,\cdot)\|_{A^0}
 \le e_j,\qquad 0\le j\le11 .
 \tag{H.4}
$$
当 $j=k$ 时直接使用原域上界，无零阶导数的额外费用。
所有候选都是同一个真误差的合法上界，所以可取最小值。
每个商必须先以有向球完成，再取上端；不能把分母的上端
当成分母下界。程序保存每个候选和被选中值。

(H.4) 没有重新计算任何原 auxiliary target 或 tail。
它给的是新阶数所需的完整误差合同。特别是不能先将
$e_0$ 当常数再数值微分；求导对象是同一全纯误差函数。
也不能把 (H.4) 授给相邻物理 piece：它只在原根所在 germ
和其已付的辅助解析延拓内成立。

## 3. 新增的有限导数列：准确递推，不作差分

对原 20 次 scalar polynomial $p$，在新的真实根闭区间 $I_*$
直接同时包围
$$
 p^{(0)}(I_*),\ldots,p^{(11)}(I_*).
$$
若 Horner 某步的导数向量是 $(v_0,\ldots,v_{11})$，
乘以 $r-r_c$ 的更新准确为
$$
 \widetilde v_0=(r-r_c)v_0+p_n,\qquad
 \widetilde v_j=(r-r_c)v_j+jv_{j-1}\quad (j\ge1).
 \tag{H.5}
$$
这里是普通导数，没有除 $j!$。全部输入区间保留原仿射参数盒。

原正弦、余弦和乘积仅扩大导数向量的长度：
$$
 (\sin b)^{(n)}
 =\sum_{j=0}^{n-1}\binom{n-1}{j}
                 (\cos b)^{(j)}b^{(n-j)},\qquad
 (\cos b)^{(n)}
 =-\sum_{j=0}^{n-1}\binom{n-1}{j}
                 (\sin b)^{(j)}b^{(n-j)},
 \tag{H.6}
$$
$$
 (fg)^{(n)}=\sum_{j=0}^{n}\binom nj f^{(j)}g^{(n-j)}.
$$
使用原 `trig_derivatives`、`derivative_product` 和同一个
512 点有向 FFT。primitive 的线性 Fourier 逆及原 parity
逐导数列作用，因它们与 $\partial_r$ 准确交换。

记得到的 unit primitive 为 $P_j$，原标量半径、高度为
$a_j,z_j$。新有限物理列为
$$
 (F_N)_j
 =\sum_{h=0}^j\binom jh a_{j-h}P_h
                  +a_j e_1+z_j e_3,\qquad 0\le j\le11 .
 \tag{H.7}
$$
最后两项只在 Fourier mean 位置加入，绝不删除真实高度或半径
mean。$P_0$ 的原两个零 mean 不意味着 $F_N$ 的 mean 为零。

(H.5)--(H.7) 是新增一次真实根区间上的有限高阶求值。
它会同时产生低阶列以完成递推，必须如实记录为新点求值；
不能将它称为复用已经算好的同一数组。已成辅助复域的所有
target、258 个完整多项式分量和导数 bounds 均不重算。

## 4. 完整 $E^{(0)},\ldots,E^{(10)}$

原固定度量是 $E=\langle F_r\cdot F_r\rangle$，
不是在未知更新面上重新定义的目标。令 $N_j$ 为新有限列
三个分量各自完整 $A^0$ 范数的共同上界。
对每对 $1\le i,j\le11$，定义准确有限零卷积
$$
 M^{N}_{ij}=\sum_m (F_N)_i(m)\cdot(F_N)_j(-m).
$$
保持 bilinear 点积，不作复共轭。原偶数 FFT 的 Nyquist 项
准确为零，故反向频率配对就是有限多项式的真正零系数；
不是把某个循环乘积的零位置冒充未付的乘积。

完整误差为
$$
 |M_{ij}-M^{N}_{ij}|
 \le 3\bigl(N_i e_j+N_j e_i+e_i e_j\bigr).
 \tag{H.8}
$$
取真实根区间时目标与固定参数 $\eta_0$ 均实，先检查有限点积的虚部包含零，
再取其真实实部并加 (H.8) 的对称实误差。这样得到
$$
 E_k=\sum_{j=0}^k\binom kj M_{j+1,k-j+1},
 \qquad 0\le k\le10 .
 \tag{H.9}
$$
三个分量和原完整 mean 都在 (H.8)--(H.9) 中。
只在这一真实实参数点使用 reality；这里没有将复 $\delta$
导致的 $u,v$ 系数设成实数，因为本阶段根本不改动它们。

每一个 $M_{ij}$ 及每个 $E_k$ 单独保存，恢复只读同源同输入
原记录。后继步骤失败时，不重新做已经成功的有限点 FFT
或 energy jet。

## 5. 精确 series 代数及真正根约束

转成除阶乘系数
$$
 A(t)=\sum_{j=0}^{11}\frac{a_j}{j!}t^j,\qquad
 \mathcal E(t)=\sum_{j=0}^{10}\frac{E_j}{j!}t^j .
 \tag{H.10}
$$
在常数项严格满足 $a_0>0,E_0>0,E_0-a_1^2>0$ 后，
用有向形式 series 的乘积、逆和正平方根递推计算
$$
 K=-\frac{A''}{A\mathcal E}
          +\frac{A'\mathcal E'}{2A\mathcal E^2},\qquad
 \beta=\frac{A'}A,\qquad
 \gamma=\frac{\sqrt{\mathcal E}}A,\qquad
 s=-A\sqrt{\frac{\mathcal E}{\mathcal E-(A')^2}} .
 \tag{H.11}
$$
这些是原固定 intrinsic 定义；$t$ 为真实旧径向坐标的增量。
$A^{(11)}$、$\mathcal E^{(10)}$ 正好足够给 $K^{(9)}$。
统一输出四个 intrinsic 量的普通导数 $0,\ldots,9$。
不把不够长的数组末端当零补齐来生成额外阶数。

新的 $K_0$ ball 应包含零；原真根证书仍提供 $K(r_*)=0$
及同一根身份。保存原新 ball 后，只有在明确标记的
`at_the_certified_true_root` 视图中才使用准确 $K_0=0$。
不得将一个任意近根点的 $K_0$ 数值强行改零。

令 $\rho=r_*-r$，则原 folded divided curvature 的准确根 series 是
$$
 k(\rho)=-\frac{K(r_*-\rho)}{\rho}
       =\sum_{q=0}^{8}
          \frac{(-1)^q K^{(q+1)}(r_*)}{(q+1)!}\rho^q
           +O(\rho^9).
 \tag{H.12}
$$
这里的负号与 $\rho$ 方向不可省。程序同时保存 ordinary $r$ jets
和这个 normalized $\rho$ series，不能混用两种规范。

新低阶 balls 必须与两个旧域保存的同一 $K,\beta,\gamma,s$ 低阶
balls 相交一致。这个检查只核对象身份；旧三阶结果不被重写，
新高阶也不从“与旧低阶相交”推出来。

## 6. 保存、恢复及后续消费的范围

本篇执行闭包固定原 object、两个 NPZ、全部真实递归源码、
原 root native、原辅助 native/process，以及新 proof/source/driver。
新 native 至少保存：

1. 原输入的完整 SHA、字节数、真实 checkout 和运行环境；
2. 一次新真实根求值的全部12个有限三分量 Fourier 列及原 scalar jets；
3. (H.4) 全部候选、每个有限范数、(H.8) 每对已接受零卷积；
4. 全部11个 energy jets、四种10个 intrinsic jets 和 (H.12)；
5. 完整检查门、成功阶段、失败前缀及实际数学运行时间。

若恢复时源、manifest、原 native 或输入身份改变，必须拒绝普通
resume。针对以后有必要的源码修复，应另立明确固定旧 source 的
迁移合同；不能放开任意跨源码恢复。

全高阶数组只作为 public Actions 的原生工件保存。
可读 process 只输出这些新标量 jets、误差及门，保持不超过60KB；
不经连接器下载二进制或改写原 native。

本篇完成后，后继 [根 Taylor 递推](R133-supplement-exact-first-Airy-root-jets-and-Taylor-tail-derivatives.md)
可以把真根 $K,\beta,\gamma,s$ 与原65/193多项式的真根完整 Fourier
列接起来计算 $F_b,F_a$、同一 $w_1$ 的根 Taylor 系数。
它本身尚不授这些幅度、不授旧 $I/J$ 或独立 even mean 的源费用，
也不授整个真实返回的 strong 常数、cutoff97 高逆、完整响应
或 Newton/PDE 存在结论。全部原物理接缝与正区端口保持独立。
