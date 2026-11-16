# 原非秩一两原子截面的十一阶真 minor 与行列式局部来源

作者：Astra-ISP-789f / normal_annihilator。AI-assisted: GPT-6 Astra Pro。  
日期：2026-11-16 UTC。

状态：**已证明，并有完整原系数的精确有理计算。** 本稿在真正 Cat 均值秩二的两原子图上，取得一个明确非空的行列式主开集。该开集内完整原临界方程恰迫二、三阶累积量等于原两原子值，因此完整第三普通矩与全部匹配 Bell 值为零。来源公式保留该行列式因子；不把这个开集结论扩大成固定均值的全部临界分类或全局 Jacobian 自然幂。

## 1. 原十七变量与真正的非秩一基点

保留 [完整第三矩 Schur 原模型](R150-appendix-six-mode-cubic-bell-third-moment-schur-reduction.md) 的六个 $y_i$、十一条物理 Hankel 坐标 $H_m$，以及

$$
R_3(y,H)=F^3-6Fb+6F\tau_2+12c-8\tau_3
-\frac12\ell^{\mathsf T}J_3^{-1}\ell.
\tag{1.1}
$$

这里

$$
F=\frac12y^{\mathsf T}Ky,\quad p=Ky,\quad
b=p^{\mathsf T}Hp,\quad c=p^{\mathsf T}HKHp,\quad
\tau_j=\operatorname{tr}((KH)^j),
$$

$$
\ell_m=[z^m](p^{\mathsf T}v(z))^3
-6[z^m]\big(v(z)^{\mathsf T}KHKv(z)\big)(p^{\mathsf T}v(z)),
\qquad v(z)=(1,z,\ldots,z^5)^{\mathsf T}.
$$

$K$ 是同一原矩阵

$$
K=
\begin{pmatrix}
0&0&0&0&5&-1\\
0&0&0&-32&5&-1\\
0&0&54&-4&5&0\\
0&-32&-4&-8&0&0\\
5&5&5&0&0&0\\
-1&-1&0&0&0&0
\end{pmatrix}.
$$

不替换为秩一限制式。原三阶 Schur 变量

$$
Z=V+\frac14J_3^{-1}\ell
$$

给完整梯度理想的准确等价

$$
(\nabla\mathcal Q_3)=(Z,\nabla R_3).
\tag{1.2}
$$

取原曲线的两个不同射影点 $x=e_0$、$z=e_5$，幅度均为一，令

$$
y_*=x+z,\qquad
H_*=\frac12(xx^{\mathsf T}+zz^{\mathsf T}),\qquad
V_*=\frac12(x^{\otimes3}+z^{\otimes3}).
\tag{1.3}
$$

$y_*$ 的 $4\times3$ Hankel catalecticant 秩为二。其两个非零端点是 $0,\infty$，不是一个曲线点的重标量。

[完整零第三矩分类](R150-appendix-nonzero-mean-zero-third-moment-critical-classification.md) §§3、5 已证明 (1.3) 属于原完整临界族。此处还在原全部系数上独立核其完整十七梯度与十六个 Schur 第三矩常项。

## 2. 固定 $H_*$ 后的全部原梯度

写

$$
H=H_*+M,\qquad M_{ij}=m_{i+j}.
$$

先对原全部 $y_i,H_m$ 求导，然后才代入 $y=y_*,H=H_*+M$。特别是在求六个原 $y_i$ 导数时，$H_*$ 保持固定；没有沿两原子参数图求导，也没有额外链式项。

按顺序定义

$$
F_0,\ldots,F_{10}
=(\partial_{H_0}R_3,\ldots,\partial_{H_{10}}R_3)
\big|_{y_*,H_*+M},
$$

$$
F_{11},\ldots,F_{16}
=(\partial_{y_0}R_3,\ldots,\partial_{y_5}R_3)
\big|_{y_*,H_*+M}.
\tag{2.1}
$$

这十七式都是关于 $M$ 的完整二次多项式，且全部常项为零。

计算使用六方向一阶有理 dual 数求导，并另由普通有理多项式构造原张量

$$
N=Fyy^{\mathsf T}-2FH
-2\big(y(Hp)^{\mathsf T}+(Hp)y^{\mathsf T}\big)
+4V_p+4HKH,
$$

$$
\Gamma=(F^2-2b+2\tau_2)y-4FHp+8HKHp
+4V(p,p,\cdot)-8V:(KHK).
$$

其中 $V=-J_3^{-1}\ell/4$。独立逐系数身份为

$$
\partial_{H_m}R_3=-6\sum_{i+j=m}(KNK)_{ij},
\qquad
\nabla_yR_3=3K\Gamma.
\tag{2.2}
$$

原物理条件仍是十一条 anti-diagonal 系数，绝不把 $N$ 整矩阵设为零。

此次实际验证覆盖全部 $17\cdot78=1326$ 个次数不超过二的原系数。所有非恒定系数另逐 $17\cdot77=1309$ 个坐标验证 primitive 整数行与原式的唯一常数比例；这些比例在 $127$ 处实际都是单位。本稿的秩与 minor 使用精确有理算术，并不依赖有限域升秩。

## 3. 实际十一阶原 $H$-minor

令

$$
L_{\nu j}=[m_j]F_\nu.
$$

实际得到

$$
\boxed{\operatorname{rank}_{\mathbb Q}L=11.}
\tag{3.1}
$$

原行基恰为 $0,1,\ldots,10$，即全部十一条原 $H$ 梯度。记其方块为 $L_H$。完整原系数上的行列式是

$$
\boxed{
\det L_H=
\frac{
1195390452331729615597514051282341579674040153395878166528000
}{
335448104013873705753780895760213
}\ne0.
}
\tag{3.2}
$$

这是原导数规范的行列式，不是 primitive 行缩放后的值。程序用 $L^{\mathsf T}$ 的 RREF 取原行，并由另一完整秩计算核对；$L_H^{-1}$ 的左右全部 $242$ 个坐标均实核为单位矩阵。

独立完整第三普通矩

$$
T_3(r)=(y^{\mathsf T}r)^3
-6(y^{\mathsf T}r)(r^{\mathsf T}Hr)+4V(r,r,r)
$$

在 (2.1) 的图上为关于 $M$ 的线性映射，全部 56 个普通三次单项式坐标的常项均为零，其 $56\times11$ 矩阵实际秩也是十一。这里不把这一个第三矩秩当作梯度秩的替代。

## 4. 有限原来源公式与固定均值的局部完整分类

十一个选中式没有常项。对每个二次单项式按最小下标抽取一个 $m_j$，确定一个仿射多项式矩阵 $C(M)$。全部原系数实际满足

$$
\begin{pmatrix}F_0(M)\\ \vdots\\ F_{10}(M)\end{pmatrix}
=C(M)
\begin{pmatrix}m_0\\ \vdots\\m_{10}\end{pmatrix},
\qquad C(0)=L_H.
\tag{4.1}
$$

令 $D(M)=\det C(M)$。由 (3.2)，$D(0)\ne0$，故 $D$ 不是零多项式。一般交换环上的伴随恒等式与 (4.1) 给出逐原来源的公式

$$
\boxed{
D(M)m_j
=\sum_{i=0}^{10}\operatorname{adj}(C(M))_{ji}F_i(M),
\qquad 0\le j\le10.
}
\tag{4.2}
$$

仿射矩阵 $C$ 的全部条目由原十七式及固定抽取规则确定，已完整保存在可重建模型中。(4.1) 的十一条多项式恒等式均实际逐系数通过。(4.2) 不依赖数值近似，也不需要将伴随矩阵全部展开才能成为确定的有限多项式证书。

每个伴随条目的 $M$ 次数至多十。因此 (4.2) 的原来源系数次数至多十；本稿不声称任何参数权费用或实际算子逆界。

设 $I_*=(F_0,\ldots,F_{16})\subset\mathbb Q[M]$。所有原式的常项为零，故 $I_*\subset(M)$。在 $D$ 可逆的局部环中，(4.2) 给反包含。因此有准确的理想等式

$$
\boxed{
I_*\mathbb Q[M,D^{-1}]=(M)\mathbb Q[M,D^{-1}].
}
\tag{4.3}
$$

所以固定 $y_*$ 后，在 $D(M)\ne0$ 的范围内，全部原临界点恰为 $M=0$，且这个受限临界方案是约化点。由 Schur 等价，完整 $(y,H,V)$ 原临界条件在该图上进一步迫 $V=V_*$。特别是 $T_3=0$，所有原匹配 Bell 值均为零。

(4.3) 没有处理 $D(M)=0$ 上可能存在的其他固定均值临界点；后者仍需真实来源或全余商信息。

## 5. 同一原物理参数图中的非空开支

这不是只对一个孤立数值点作结论。取

$$
u(s)=(1,s,\ldots,s^5),\qquad
w(t)=(t^5,t^4,\ldots,1),
$$

$$
x=a u(s),\qquad z=b w(t),\qquad ab(1-st)\ne0.
$$

两个物理点不同，且两幅度非零。令

$$
y=x+z,\quad
H_0=\frac12(xx^{\mathsf T}+zz^{\mathsf T}),\quad
V_0=\frac12(x^{\otimes3}+z^{\otimes3}).
\tag{5.1}
$$

原十七梯度先求完后代入 $H=H_0+M$，记为 $\mathcal F_\nu(a,b,s,t;M)$。原完整两原子临界族保证它们的 $M$ 常项在整个参数图上恒等为零。仍选原十一条 $H$ 梯度，并使用 (4.1) 的同一抽取规则，得到有理系数的多项式矩阵

$$
\mathcal F_H=\mathcal C(a,b,s,t;M)M.
\tag{5.2}
$$

在 $(a,b,s,t,M)=(1,1,0,0,0)$，其常 minor 正好是 (3.2)。故 $\mathcal D=\det\mathcal C$ 非零，且

$$
ab(1-st)\mathcal D\ne0
\tag{5.3}
$$

是一个明确非空的参数主开支。在这个环中，十七原梯度的理想恰为 $(M)$；加入原 Schur 变量后完整理想恰为 $(M,Z)$。全部完整临界点都为 (5.1)，不存在 $T_3$ 本质维数四、五、六的临界点。

这里参数图是对原物理均值秩二部分的明确拉回。没有宣称它在原十七维空间全局可逆，也没有以此处理 Cat 秩三均值。

对于任一固定匹配方向 $r$，原 Schur Bell 形式 $B_r$ 关于 $M$ 为一次式，并在 $M=0$ 为零。因而 (5.2) 同样给

$$
\mathcal D B_r\in(\mathcal F_0,\ldots,\mathcal F_{16}),
\tag{5.4}
$$

来源由 $B_r$ 的十一条线性系数乘 $\operatorname{adj}\mathcal C$ 确定。这个行列式因子没有已付实际算子可逆性，不能从 (5.4) 跳到全局自然幂或整体 Hilbert 问题结论。

## 6. 实际执行、全部检查与可重现身份

数学执行是 GitHub Actions run **43799163632**、job **133074883011**，步骤 **original-two-atom-seventeen-gradients**；执行源提交为 **8caed8c2e733fa2a5cfb6338ef62311aaf3ecf10**。完成状态为 success / exit 0。

[完成 job 的实际日志](https://github.com/Rogerhu12/math-research-public/actions/runs/43799163632/job/133074883011) 给：

| 检查 | 实际结果 |
|---|---:|
| 原 $K$ 物理曲线系数 | 全部零 |
| 原 $J_3^{-1}$ 左右乘积 | 512 个坐标全真 |
| 原十七梯度完整系数 | 1326 个坐标全真 |
| primitive 整数行运输 | 1309 个坐标全真 |
| 原完整临界常项 | 17 条全真 |
| 原第三累积量常项 | 16 条全真 |
| 完整普通第三矩 | 56 坐标保留，线性秩 11 |
| 原梯度线性矩阵 | $17\times11$，秩 11 |
| 实际原行选择 | $0,\ldots,10$ |
| 完整仿射来源身份 (4.1) | 11 条全真 |
| 原常 minor 左右逆 | 242 个坐标全真 |

精确构造用时 **0.250180252 秒**，外层墙时 **0.314388939 秒**；未构造大 Macaulay 矩阵，未用有限域秩。

源码：

- [完整自足生成器](../notes/2026-11-16-r150-original-nonrankone-two-atom-gradient-789f.py)，Git blob 948d3c17f90ee17c9b0b773d981c3189674b47d5，22167 B，SHA256 3729a351a361039e286b2435571da8c2c91d09d9822cc79cacb9cecf887928cc。
- [冻结参数](../notes/2026-11-16-r150-original-nonrankone-two-atom-gradient-inputs-789f.json)，Git blob f9dde78016579b4b327ea4be29ae683858a7e603，2429 B，SHA256 2e2948108dc8a17fe1657cdd69d58b99b760017e9da6d2843d7d24ef07a14efb。
- [完整接口与边界](../notes/2026-11-16-r150-original-nonrankone-two-atom-gradient-interface-789f.md)。

实际原模型的逻辑数据为 173045 B，SHA256

~~~text
1f93dcd7db76f433df57536d4bd0b51417ae2a12137e08136141b4a9689a8d8d
~~~

其临时 gzip 为 47898 B，SHA256

~~~text
c3421249e50716fe19d45ded2da7b40483f5d3321b5479f3f2edf94aa251b5ef
~~~

实际小回执为 2792 B，SHA256

~~~text
8417b4b63249932a9b22db324e882e78dd4b28af4fd155511acb7294dec52664
~~~

语义 binding 为

~~~text
2343a3e3f632236b0a5dc425f30a5f1ce27bfd10ff4add1d4c30c75ae692bcf9
~~~

原系数、线性矩阵和第三矩图的 SHA 分别为

~~~text
d7056c0546a4b1379a019d70e7f81632539e4866c7e3e5bddde0da1b27692832
48708f39da70539929308f20e710907d5c0bce411b47e2a84783ed7e8406462d
065706fcc695fd03762a049c03949e3b42f806845606aa228de0324e18017aa5
~~~

[仓库执行身份文件](../notes/r150-nonrankone-execution-789f/43799163632-original-two-atom-seventeen-gradients.json) 只保存源码、参数、run 与输出 SHA；按规则15，没有把可重建的数学数组或完整计算输出新增入仓库。实际数学数据取自上述已完成 job 日志。

## 7. 下一原接口

已经支付的是 (4.2)–(5.4) 的真实行列式局部来源。下一可复用同一十七式，构造全部次数至多三的原乘子，得到 $6188$ 个原来源到次数一至五的 $4367$ 个目标单项式的完整矩阵。

若其真实有限域秩达到 4367，便可由一个真实非零原 minor 升到特征零，证明固定均值的整个 $(M)$ 已由原方程生成；相应参数分母将只依赖两原子参数，不再依赖 $M$。这项全矩阵秩尚未计算，本稿不预填其值。若未满秩，则须保真实余商后继续，而不是据局部 minor 宣布剩余截面为空。
