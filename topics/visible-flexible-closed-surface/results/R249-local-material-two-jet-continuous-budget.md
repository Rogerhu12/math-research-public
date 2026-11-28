# R249：保留角向重参数抵消的局部连续二 jet 预算

2026-11-28，Astra-visible-flex-2ecfcd69-20261128。

**状态：以下连续充分条件与算法已证明；非零两片实现检查已实际执行。尚未用它证明新的研究场合格，不宣称精确等距或 README 第5条完成。**

## 1. 对象及与已有结果的区别

沿用 R226/R230 的原准确 M12 源 $X$、原固定度量 $g$、确定中央归一差 $C$ 及实际保存修正 $W$。新场始终是

$$
Y=X+C+W.
$$

本条不改变 $X,C,W,g$ 或相位区间。R236 已利用局部径向尺度、Bernstein 共同权及 Fourier 平方范数收紧一阶估计；这里补充完整材料二阶导数，特别是把角度反参带来的两个项先在 Fourier 系数层合并。

共同图写为 $q=Tz$、$ds=H(q)\,dq$；角图是原中央准确弧长角，

$$
du=\frac{J(\theta)}a\,d\theta,\qquad
P(\theta)=J(\theta)^2=|\gamma_\theta(\theta)|^2,\qquad
a=\frac1{2\pi}\int_0^{2\pi}J.
$$

$P$ 是已知的准确有限 Fourier 多项式，严格 $a$ 盒与 $J_{\min}>0$ 使用 R226。角图与 $z$ 无关。节点和 binary64 系数按准确实数解释；中央及真正平 cuff 的 $W$ 两 jets 为零。内部可为五次 $C^4$ 或 $C^2$ 样条，只需其节点重数不超过三。

## 2. 完整链式法则及抵消

直接微分得到

$$
W_s=\frac{W_z}{TH},\qquad
W_u=\frac{aW_\theta}{J},
$$

$$
W_{ss}=\frac{W_{zz}}{T^2H^2}-\frac{H_qW_z}{TH^3},
\qquad
W_{su}=\frac{aW_{z\theta}}{THJ}.
\tag{1}
$$

对角向再次微分，

$$
W_{uu}
=\frac{a^2W_{\theta\theta}}{J^2}
-\frac{a^2J_\theta W_\theta}{J^3}
=a^2\,\frac{P W_{\theta\theta}-P_\theta W_\theta/2}{P^2}.
\tag{2}
$$

式 (2) 只是恒等改写，没有近似。记

$$
\mathcal N(W)=P W_{\theta\theta}-\frac12P_\theta W_\theta.
$$

若 $P=\sum_k p_ke^{ik\theta}$、某个复平面坐标或实高度的 Laurent 系数为 $W=\sum_m w_me^{im\theta}$，则

$$
\mathcal N(W)
=\sum_{k,m}p_kw_m\left(-m^2+\frac{km}{2}\right)e^{i(k+m)\theta}.
\tag{3}
$$

因此 $\mathcal N(W)$ 仍是有限 Fourier 多项式。先用 (3) 合并同频系数，再求向量平方范数，可以保留旧 $U_1^2|W_{\theta\theta}|+U_2|W_\theta|$ 三角界丢掉的抵消。

## 3. 同一组 Bernstein 权控制全部项

在径向片 $[b_0,b_1]$，准确 Boehm 插入给

$$
W(z,\theta)=\sum_{i=0}^5 B_i^5(\xi)C_i(\theta),
\quad
\xi=\frac{z-b_0}{b_1-b_0}.
$$

对 $z$ 一次、二次微分后，按标准升阶恒等式把四次、三次 Bernstein 表示升回五次。于是有完整控制行 $D_i,E_i$，满足

$$
W_z=\sum_i B_i^5D_i,\qquad W_{zz}=\sum_i B_i^5E_i.
$$

各角导数以及 $\mathcal N$ 只对 $\theta$ 作用，故与这些相同非负权可交换。令该片严格有

$$
TH\ge L>0,\qquad f\ge f_*>0,\qquad
\frac{|H_q|}{TH^3}\le B.
$$

在每个角盒 $I$ 内，设

$$
\begin{aligned}
&P\ge P_*>0,\quad
|C_i|\le c_i,\quad |D_i|\le d_i,\quad |E_i|\le e_i,\\
&|C_i'|\le t_i,\quad |D_i'|\le v_i,\quad
|\mathcal N(C_i)|\le n_i .
\end{aligned}
$$

所有下列量均可分别对 $i$ 和角盒取最大值：

$$
\|W\|_\infty\le\max_i c_i,
\tag{4}
$$

$$
\left(|W_s|^2+\frac{|W_u|^2}{f^2}\right)^{1/2}
\le
\max_i\left(\frac{d_i^2}{L^2}
+\frac{a_+^2t_i^2}{f_*^2P_*}\right)^{1/2},
\tag{5}
$$

$$
|W_{ss}|+\frac{2|W_{su}|}{f}+\frac{|W_{uu}|}{f^2}
\le
\max_i\left(
\frac{e_i}{L^2}+B d_i+
\frac{2a_+v_i}{Lf_*\sqrt{P_*}}
+\frac{a_+^2 n_i}{f_*^2P_*^2}
\right).
\tag{6}
$$

式 (4) 来自范数凸性。式 (5) 把两个一阶导数组成同一六维向量后使用平方范数凸性。式 (6) 对 (1)—(2) 的各向量项取范数，利用同一组 Bernstein 权，再取最大控制行。因此这不是把若干抽样最大值当作全域界；它覆盖径向片内部和端点。节点两侧的连续二 jet 使闭片并集覆盖完整 $C^2$ 场。

若片与首 ramp 相交，分别把 R226 对 $C$ 的准确位移、一阶及二阶组合界加入 (4)—(6)；其余片不加入 $C$。在 $C$ 支撑上 $f\ge1$，因此无需给 $C$ 乘尾端最小半径因子。

## 4. 局部径向尺度

严格 $L,f_*$ 使用 R236 已证明的同一原图计算。前缀 $H=1$，所以 $H_q=0$。在尾部，

$$
r=c-hR(t),\qquad t=(q-S)/h,\qquad
H=R'(t)\sqrt{1+w(r)^2}.
$$

于是

$$
H_q=\frac{R''(t)}h\sqrt{1+w^2}
-R'(t)^2\frac{w w_r}{\sqrt{1+w^2}}.
$$

原全尾的 $|w|\le16/15$、$|w_r|<24$ 和 $\sqrt{1+w^2}<3/2$ 给

$$
|H_q|
\le \frac{3}{2h}\sup_I|R''|
+24\frac{16}{15}\left(\sup_I|R'|\right)^2.
\tag{7}
$$

片内 $R',R''$ 是区间系数多项式，以准确 Bernstein 限制取界；再与 R226 的全域 $60$ 取较小者。若片跨前缀/尾接口，对两部分合取，前缀导数为零。$T$ 与接口 $S$ 使用原准确根盒，未把浮点接口当准确端点。

## 5. 完整 Fourier 平方范数、区间及舍入预算

平面复坐标的模方和实高度 Laurent 多项式的模方相加即向量平方范数，交叉项全部由自相关保留。D3 及反射对称使其为 $x=3\theta$ 的实偶余弦多项式。故沿用 R236 的整数 Taylor 闭盒覆盖 $x\in[0,\pi]$，由对称覆盖全角。

对于任意平方范数多项式，先求准确整数 Fourier 系数，再由 R236 的明确 Taylor 余项向外包界。开平方也由整数区间运算完成。$P$ 的每盒下界扣除自身系数格点化误差，并与 $J_{\min}^2$ 合取。

实现把 $P$ 和控制向量系数向下取为 $2^{-96}$ 格点。设 $P^\flat,C^\flat$ 为格点化多项式，记

$$
e_{P,j}=\sum_k |k|^j|p_k-p_k^\flat|,
\quad
e_{C,j}=\sum_m |m|^j|c_m-c_m^\flat|.
$$

向量系数的和按平面与高度两部分的绝对和取，故同时控制欧氏范数。将两个乘积各加减一次可得

$$
\begin{aligned}
\|\mathcal N(C)-\mathcal N^\flat(C^\flat)\|_\infty
\le{}&
e_{P,0}\|C''\|_{\ell^1}
+\|P^\flat\|_{\ell^1}e_{C,2}\\
&+\frac12e_{P,1}\|C'\|_{\ell^1}
+\frac12\|(P^\flat)'\|_{\ell^1}e_{C,1}.
\end{aligned}
\tag{8}
$$

右侧所有量由准确系数或有理绝对和给出。(8) 在对格点化 $\mathcal N$ 求模方并开平方后加入；不遗漏多项式乘法中的舍入误差。其余导数同样加入对应 $e_{C,j}$。算法中的浮点数只供显示或从已保存 binary64 读取准确有理数，不参与严格不等式判定。

## 6. 全闭面及全部相位的几何传递

令 (4)—(6) 加中央差后在所有片的最大值为 $\eta,p,c_w$。使用 R230 对原完整源的 $c_X$ 以及 R234 的原常数 $d,K_0,R$，定义

$$
\epsilon=d+2(1+d)p+p^2,\qquad
\nu=\frac{3p+p^2}{1-d},
$$

$$
K=\frac{K_0(1+d)+\nu c_X+c_w}{1-\epsilon},
\quad
\sigma=.737-1.9\nu-\eta,\quad
D_*=2(R+\eta).
\tag{9}
$$

若 $\epsilon<1$、$\eta<1/K_0$、$R+\eta<2$、$\sigma>1/K$，且 R234 的固定标记管邻域及三阶矩损失条件保持，则沿整个 $X+v(C+W)$ 同伦都满足相同充分条件。R10 的正支撑平行面定理给全局嵌入及 reach，而非只给局部曲率半径。具体地，

$$
\frac{\operatorname{reach}}D\ge\frac1{K D_*},\qquad
\frac{\delta_{\rm hold}}D
\ge\frac{.19989114-2\eta}{D_*}.
$$

原固定帽和对称性未动；R16 的完整欧氏群矩不变量仍按 R234 消费。完整相位作用是空间旋转加均匀材料角平移，保持原 $g$，故所有空间上确界和几何结论覆盖整个相位区间。若数值不等式未通过，只说明该充分预算不足，不推出真实 reach 不足或不存在精确解。

本条仍未使用 $DX$ 与 $dW$ 的 cross-Gram 抵消，也没有把 $W$ 的切向二阶部分从法向投影中扣除。它进一步收紧二 jet 预算，但并非最终最佳界。

## 7. 实现与已执行范围

实现为 scripts/2ecf-m12-local-material-two-jet-budget.py。它核对真实 field/grid/result、R226 连续差报告、R230 全源报告及原 prefix/bridge/manifest 的身份；只有全部一致才计算。输入与大输出只保在临时运行目录。

非零实现检查 scripts/2ecf-m12-local-material-two-jet-fixture.py 使用原准确中央 $J$、一个非零径向自由行、74 个完整角通道和两片五次样条。其人工坐标取 $a=1,s=z,f=1$，不冒充生产 M12。独立 SciPy 样条微分和直接材料链式公式在 12,545 点比较；直接链式式 (2) 与先合 Fourier 分子的最大差约 $4.6\times10^{-20}$，所有样本落在准确连续界内。完整连续性的根据是第2—5节的证明，有限检查只检验实现接口。

这份接口成功不能替代研究场消费。后续须读取本轮实际保存场，给出其新连续界，并继续原固定 $g$ 的真实误差加密。
