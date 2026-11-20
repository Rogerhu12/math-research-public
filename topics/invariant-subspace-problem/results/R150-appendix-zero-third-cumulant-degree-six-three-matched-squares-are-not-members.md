# R150 附录：零第三累积量完整消元理想中的三份匹配 Bell 平方均非成员

日期：2026-11-20（UTC）。作者：Astra-ISP-b2a9acde-20261120（root 与 literature）；AI-assisted GPT-6 Astra Pro。

**状态：以下特征零非成员性已证明。** 在原 $V=0$、非零均值最高式确定的六变量图上，保留全部十一条原二阶梯度和全部六条原均值梯度。原三个指定匹配 Bell 三次式的自然平方，分别不属于这个完整六变量消元理想；更强地，统一代数参数表示中出现的三份有理六次系数目标，在该理想的六次商空间中线性独立。

这不是仅凭一个模素数失败作出的结论。本次源矩阵有恰好 267 列，其模 $103$ 秩达到全部 267；增广矩阵有恰好 270 列，其模秩也达到全部 270。两项平凡列数上界将两个特征零秩都夹定。

本稿不证明匹配 Bell 值在 $V=0$ 临界集上非零，也不排除更高自然幂证书。后续继续检验新的三次自然幂及其他完整来源。

## 1. 原最高式的六变量图与完整低梯度理想

保留 [原六模式 Schur 稿](R150-appendix-six-mode-cubic-bell-third-moment-schur-reduction.md) 的 $K$、十一阶可逆 $J_2$ 及原 Hankel 累积量坐标。令
$$
p=Ky,\quad
\mathbf d_2(y)=[z^m](p^{\mathsf T}v(z))^2_{m=0}^{10},
\quad
H(y)=\operatorname{Hankel}\!\left(\tfrac16J_2^{-1}\mathbf d_2(y)\right).
\tag{1.1}
$$
在 $V=0,\ y\ne0$ 时，原完整最高式
$$
(p^{\mathsf T}v(z))
\left((p^{\mathsf T}v(z))^2
-6v(z)^{\mathsf T}KHKv(z)\right)=0
$$
在多项式整环中准确约去非零一次极线，给出 (1.1)。原 $y=0$ 点不必满足这个图关系，但其全部匹配三次 Bell 值本来就为零；本稿没有丢弃这部分后再据此宣称整个临界层为空。

在 (1.1) 中写
$$
F=\tfrac12y^{\mathsf T}Ky,\quad
h=Hp,\quad b=p^{\mathsf T}Hp,\quad
\tau_2=\operatorname{tr}((KH)^2).
$$
原完整均值梯度除去可逆常数因子后的六个分量为
$$
\Gamma=(F^2-2b+2\tau_2)y-4FHp+8HKHp.
\tag{1.2}
$$
这里最后一项按矩阵次序是 $8H K H p$。原二阶梯度矩阵为
$$
N=Fyy^{\mathsf T}-2FH
 -2(yh^{\mathsf T}+hy^{\mathsf T})+4HKH.
\tag{1.3}
$$
令
$$
n_m(y)=[z^m]\,v(z)^{\mathsf T}KNKv(z),
\quad 0\le m\le10.
\tag{1.4}
$$
准确使用 [原完整低阶梯度稿](R150-appendix-four-jet-complete-low-gradients-and-projected-quadric.md) 的全部坐标。定义
$$
I_0=(n_0,\ldots,n_{10},\Gamma_0,\ldots,\Gamma_5)
 \subset\mathbb Q[y_0,\ldots,y_5].
\tag{1.5}
$$
$H(y)$ 二次齐次，因此 $n_m$ 四次、$\Gamma_i$ 五次。没有对 Cat 秩、$H$ 秩、支撑、均值位置或临界零点作额外限制。

## 2. 原三个指定目标及统一有理系数展开

原匹配方向的准确身份在 [本质维数至多三完整稿](R150-appendix-all-essential-cubic-dimensions-at-most-three-have-zero-matched-bell-values.md) §4。令 $d_1,d_2,d_3$ 为原三次式
$$
P(d)=3725d^3-43931504d^2
       +6080833024d+52565262336
\tag{2.1}
$$
的三个指定实根，并置
$$
A(d)=-\frac{521d^2-46784d+271360}{160(5d-704)},
\quad B(d)=A(d)+d,\quad
r(d)=(A(d),B(d),0,0,0,1).
\tag{2.2}
$$
该分母在所有三根处非零；生成器还在
$\mathcal A=\mathbb Q[d]/(P)$ 中准确求逆并核乘积为一。

原完整 Bell 值在 $V=0$ 的图上为
$$
S_{r(d)}(y)=(r(d)^{\mathsf T}y)^3
-6(r(d)^{\mathsf T}y)\,r(d)^{\mathsf T}H(y)r(d).
\tag{2.3}
$$
自然平方在自由三维有理代数 $\mathcal A$ 中唯一写成
$$
S_{r(d)}(y)^2=t_0(y)+d\,t_1(y)+d^2t_2(y),
\qquad t_j\in\mathbb Q[y]_6.
\tag{2.4}
$$
这里是自然平方，不是第六阶普通 Bell 多项式。

程序按 (2.1)–(2.4) 直接构造目标。它另外用原 $W_\pm$ 的规范基及原两个 conic 核验
$Q_\pm(E_\pm^{\mathsf T}r(d))=0$，但这些辅助恒等式不代替 (2.2) 对三个指定目标的身份绑定。

## 3. 六次理想来源恰好是 267 列

记 $R_e=\mathbb Q[y_0,\ldots,y_5]_e$。由 (1.5) 的齐次性，
$$
(I_0)_6
=\sum_{m=0}^{10}R_2\,n_m
 +\sum_{i=0}^5R_1\,\Gamma_i.
\tag{3.1}
$$
即使最初允许任意次数的多项式乘子，取等式的六次齐次分量也准确得到 (3.1)，不会产生遗漏来源。

六次单项式数为
$$
\dim R_6=\binom{11}{5}=462.
$$
全部来源列数为
$$
11\binom75+6\binom65
=11\cdot21+6\cdot6=267.
\tag{3.2}
$$
生成器保留所有这些列和全部 462 行。各原有理生成元、各有理目标系数只分别乘一个非零有理数，以清分母及除整数内容；这些操作是特征零单位，不改变来源空间或目标商空间的线性独立性。

令 $M\in\mathbb Z^{462\times267}$ 是该完整来源矩阵，令
$\widetilde t_0,\widetilde t_1,\widetilde t_2\in\mathbb Z^{462}$
是三份相应 primitive 整数目标。增广矩阵为
$$
\widehat M=[\,M\mid\widetilde t_0\mid
 \widetilde t_1\mid\widetilde t_2\,]
 \in\mathbb Z^{462\times270}.
\tag{3.3}
$$

## 4. 实际执行记录及特征零秩夹逼

[固定 degree-six 生成与验证器](../notes/2026-11-20-r150-vzero-degree-six-matched-bell-certificate-b2a9.py)
已在 [Actions run 44731129539](https://github.com/Rogerhu12/math-research-public/actions/runs/44731129539) 的 job 136270857160 中实际执行，标签为 vzero_degree6。冻结提交77d32165a6d85885e799c1b5c34712c60dd25a30；运行在2026-11-20 11:52 UTC完成，程序自身记录约1.026秒，最高RSS 52780 KiB。[批次运行身份](../notes/2026-11-20-exact-source-run44731129539-b2a9.json)保完整日志SHA、真实pull与各独立子进程身份；该批次另一源码的失败不影响本程序全部完成的结果。

本次全部原来源控制通过，包括原 $K,J_2$ 绑定、全部最高系数的有理解、$\tau_2=b/6$、所有低梯度在原物理均值曲线上的恒等控制，以及三个目标的原两 conic 有理核验。精确模结果为
$$
\boxed{\ \operatorname{rank}_{\mathbb F_{103}}M=267,\qquad
\operatorname{rank}_{\mathbb F_{103}}\widehat M=270.\ }
\tag{4.1}
$$
所选源单位子式为 $267$ 阶，行列式模 $103$ 等于 $83\ne0$。

绑定本次实际整数对象的 SHA256 为：

| 对象 | SHA256 |
|---|---|
| 执行源 | baa36d716e7f15b2a6ba7f3739cebdf3f5e6d98b9f4e305bf1a2c9716125ff54 |
| 完整 $M$ | 3b2be5906b7c3d6a19b9c78587c7017c08cda31b5a86af17c6afd22c43ce63aa |
| 完整三目标列 | a57d33e6f30ed02e5faca7037d22dd4e372ecff2441e56f11662d41a9ef33584 |
| 原 $H(y)$ | 24988090a2fc366b326e4a0abfe28cd913b7fb5d965e7341d46036b524773485 |
| 原全部十七个低梯度 | bf44e23c3b67677b08024f22c66f1155b87f4babf3d4341014f6b7a3e52da1dc |
| 程序标准输出 | 59fff8d17833ba785069c4c3264b9826edcf002be3a66bc86cef36599a356653 |

整数矩阵的模素数非零子式在 $\mathbb Q$ 中仍非零。因此 (4.1) 给两个有理秩下界。另一方面，(3.2)–(3.3) 的完整列数分别给有理秩上界 267 与 270。故准确有
$$
\boxed{\ \operatorname{rank}_{\mathbb Q}M=267,\qquad
\operatorname{rank}_{\mathbb Q}\widehat M=270.\ }
\tag{4.2}
$$

本次程序没有执行有理乘子求解；日志中的通用“没有宣称特征零非成员”字段只是生成器对一般模失败所采取的保守输出。(4.2) 是根据这一次已经达到全部列数的实际秩另作的完整数学提升，没有声称不存在的 QQ 求解运行。

由 (4.2)，
$$
[t_0],[t_1],[t_2]\in R_6/(I_0)_6
\tag{4.3}
$$
线性独立。

## 5. 每个原匹配方向的平方都非成员

有理矩阵的列秩在标量扩张至 $\mathbb C$ 后不变。因此 (4.3) 在复数商空间中仍线性独立。对任何指定根 $d_j$，(2.4) 的系数组为
$$
(1,d_j,d_j^2),
$$
其第一项为一；清分母与 primitive 化只把三项分别再乘非零有理单位。因此它是三份独立商类的一个非零线性组合，不可能为零。

结合 (3.1)，对每个 $j=1,2,3$ 得到
$$
\boxed{\ S_{r_j}(y)^2\notin
 I_0\,\mathbb C[y_0,\ldots,y_5].\ }
\tag{5.1}
$$
这里没有把“统一参数中的一个系数目标失败”误读成“三个代数根目标都失败”：结论用的是三份有理目标模完整来源的共同线性独立性。

## 6. 这一结果没有关闭什么

式 (5.1) 排除的是当前完整 $V=0$ 消元理想中的自然平方证书。它不排除 $S_{r_j}$ 属于该理想的根基，不排除自然三次或更高幂，也不产生任何 Bell 非零的临界点。

因而本稿不会将计算改述成普通 ISP 反例、全临界集非空证据、或更高本质维数的空性。下一项新的固定目标是同一完整六变量理想中的 $S_{r_j}^3$，其九次来源为 2002 行、3528 列；这与重新运行本稿已关闭的六次检验不同，且仍必须核原全部来源和特征零正证书。
