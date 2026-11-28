# R150 补充：正确整 B 原图的全头胶合与完整 I6 十二行两列表示

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。AI-assisted，GPT-6 Astra Pro。

## 1. 完整适用范围

保持当前正确 unit211 的
$$
\Phi=0,\qquad Q(1-Q)P_fP_{02}bcD\ne0,
$$
并取整个正确三均值首项曲线
$$
B=-Q^2+(12u^2-20u+8)Q-16(u-1)^2=0.
$$
沿[已付双向有理图](R150-appendix-unit211-Phi-zero-true-Bzero-rational-and-exact-six-by-two-model.md)，写
$$
u=\frac{(x+1)^2}{3x},\qquad Q=\frac{4F}{3},
$$
$$
F=x^2-x+1,\quad H=2x-1,\quad \beta=5x-1,\quad J=7x^2-4x+1.
$$
内在原参数给 $xF(x+1)H\beta J\ne0$；[整个斜率二次纤维排除](R150-appendix-unit211-Phi-zero-true-Bzero-slope-quadratic-complete-original-exclusion.md)另给
$$
C_2=23x^2-11x+2\ne0.
$$
令
$$
A=\mathbb Q[x,1/(xF(x+1)H\beta JC_2)],\qquad R=A[\lambda].
\tag{1}
$$

本条得到整个 B 图上完整原六条件的精确十二行两列表示。先前三次头 $H_3=11x^3-18x^2+6x-1$ 从未被倒置，其整个零纤维由本次全头胶合覆盖。本条没有排空整个 B，也没有证明所有固定权处的 $\lambda$ 都有限。

## 2. 同一原 Gram 的六个条件

原自由变量取 $(\lambda,f,t)$，真实恢复为
$$
\ell=\frac{(x+1)\beta}{6x^2},\quad \delta=1-Q=-H^2/3,\quad
bc=\frac{(x+1)^2J}{36x^4},
$$
$$
K_0=\frac{4F(x+1)}{3x},\quad T_0=-K_0,\quad
P_{02}=\frac{4F^2(x+1)\beta}{27x^3},
$$
$$
T=\frac{3(x+1-f)}{\beta}-\frac{x+1}{x}\lambda-\ell,
$$
$$
A_1=\frac{2F(f-x-1)}{3x^2}
+\frac{2F(x+1)\beta}{9x^3}\lambda.
\tag{2}
$$
置 $V=f-A_1/2+bc\,t,\ W=-K_0/2+2uf,\ m=u-\ell,\ M=4bc\delta$，则
$$
x_0=\frac{(u-\ell Q)V-mW}{M},\qquad
y_0=\frac{\ell W-uV}{M},\qquad X=x_0+\rho y_0,\quad Y=x_0-\rho y_0,
$$
$$
\rho^2=\delta,\qquad
b=\frac\ell2-\rho\,\frac{(x+1)(x-1)}{4x^2H},\quad c=\bar b,\quad
p=1+\rho,\ q=1-\rho.
$$
令 $a=1-\ell,\ r=X-ap-ct,\ s=Y-aq-bt$。完整四行 Gram 是
$$
(0,0,p,q),\quad(0,A_1,r,s),\quad(p,r,0,t),\quad(q,s,t,0).
\tag{3}
$$
全过程使用真实 dual 乘法 $(vw)_1=v_0w_1+v_1w_0$，没有使用旧错误 compact germ。

从 (3) 定义原条件
$$
F_0=E_1,\quad F_1=E_{\rm e},\quad F_2=E_{\rm o},\quad F_3=N_1,
$$
其中 $E_B=E_{\rm e}+\rho E_{\rm o}$。另保完整 weighted $NS,PS$。源已把原 $E_0,N_0,P_1$ 的恢复和六个值逐项返回。记
$$
I_4=(F_0,F_1,F_2,F_3),\qquad I_6=I_4+(NS,PS).
$$

## 3. 全四头的原 adjugate 胶合

按 $(1,f,t,f^2,ft,t^2)$ 展开四式，写
$$
\boldsymbol F=L(1,f,t)^{\mathsf T}+H_{\rm q}(f^2,ft,t^2)^{\mathsf T}.
$$
$H_{\rm q}$ 是四乘三、仅依赖 $x$ 的真实头矩阵。对其四个固定三阶子式取共同原分母 $d$，令对应多项式为 $d_i$。本次完整 QQ[x] Bézout 返回
$$
\sum_i b_i d_i=g,\qquad
\boxed{g=(x+1)^3F^4.}
\tag{4}
$$
首个三阶子式在整个 B 上为零，仍在此完整族中保留。所有分母和 (4) 的 $g$ 都仅含内在原权单位。

若 $H_i$ 表示选定的三行，利用插入回四列的 adjugate，定义
$$
J_{\rm q}=\sum_i \frac{b_i d}{g}\operatorname{adj}(H_i)\operatorname{pr}_i.
$$
本次逐项返回全部九个条目
$$
J_{\rm q}H_{\rm q}=I_3.
$$
从而三条完整原身份为
$$
(f^2,ft,t^2)^{\mathsf T}
+J_{\rm q}L(1,f,t)^{\mathsf T}
=J_{\rm q}\boldsymbol F.
\tag{5}
$$
所以全 B 的原四式商（包含 $N_1$）由 $1,f,t$ 生成。这里不假模自由，也没有删掉临时主元或 $H_3$ 零集。

## 4. 原均值线性关系与中心坐标

取原三个均值的完整左核组合
$$
\kappa=\bigl(-18x^3H,\ 
2-13x+54x^2-79x^3+68x^4,\ 
H(-2+15x-54x^2+97x^3-48x^4)\bigr).
$$
本次直接从原式返回
$$
L_0=\kappa_0F_0+\kappa_1F_1+\kappa_2F_2
=(a_1\lambda+b_1)f+(c_1\lambda+d_1)t+
A_2\lambda^2+B_2\lambda+C_0,
\tag{6}
$$
其 $f,t$ 二次头全部为零。真实
$$
\Delta=a_1d_1-b_1c_1
$$
仅有 (1) 已付因子，因此在 A 中是单位；本次所有分母均实际剥到 (1)。

令
$$
\omega=a_1f+c_1t+A_2\lambda+B_2.
$$
由 (6) 的可逆二乘二恢复，
$$
f=\frac{(c_1\lambda+d_1)\omega-A_2d_1\lambda+c_1C_0-d_1B_2}{\Delta},
$$
$$
t=\frac{-(a_1\lambda+b_1)\omega+A_2b_1\lambda+b_1B_2-a_1C_0}{\Delta}.
\tag{7}
$$
因此模原关系 $L_0$ 的坐标变换是双向的，不是只选取某个原解的形式参数。

把 (5) 按 $a_1^2,2a_1c_1,c_1^2$ 组合并作 (7) 得
$$
q(\omega)=\omega^2+q_1(\lambda)\omega+q_0(\lambda)\in I_4,
\tag{8}
$$
完整四原乘子已返回。实际次数为
$$
\deg_\lambda q_0=2,\qquad\deg_\lambda q_1=1.
\tag{9}
$$

## 5. 精确 I6 与十二行

四个原二次经 (7) 代入后，减其 $\omega^2$ 系数乘 (8)，得到线性余式 $\ell_0,\ldots,\ell_3$。完整原 $NS,PS$ 在最后一次代入 (7) 后按首一 q 作短除，得到线性 $n_\omega,p_\omega$；每次商乘 q 加余式均完整返回。因此在 (6) 消去后的同一个环中有精确理想身份
$$
\boxed{I_6=(q,\ell_0,\ell_1,\ell_2,\ell_3,n_\omega,p_\omega).}
\tag{10}
$$
$R[\omega]/(q)$ 本身以 $(1,\omega)$ 为自由基。对任一线性行 $(r_0,r_1)$，其真实 $\omega$ 倍为
$$
(-q_0r_1,\ r_0-q_1r_1).
\tag{11}
$$
六条线性行与各自 (11) 给十二行。任意多项式乘子模 q 都为 $a+b\omega$，所以这十二行作为 R 子模恰好生成 (10) 的理想像。这证明完整原商是该十二乘二矩阵的余核；并未假设最终商自由或无扭结。

本次实际十二行的两列 $\lambda$ 次数依次为
$$
(4,3),(5,4),\ (4,3),(5,4),\ (4,3),(5,4),\
(3,2),(4,3),\
(6,5),(7,6),\ (6,5),(7,6).
\tag{12}
$$
其中首四对来自四原二次，末两对来自完整 NS、PS。

## 6. 三个真实标量必要式与范围

把六条未乘 $\omega$ 的线性行编号为 $0,\ldots,5$。本次实际取
$$
(0,4),\quad(0,5),\quad(4,5)
$$
三对固定二列 cofactor，得到非零原标量式，其 $\lambda$ 次数分别为
$$
9,\quad9,\quad10.
\tag{13}
$$
它们由两条原行的交叉组合直接落在 (10) 中；清分母只用 (1)。所有未付首项零纤维保留。因此 (13) 本身还不提供全 B 的首一 $\lambda$ 环境，也不提供全图排空。

本条完全覆盖旧 $H_3=0$，但不恢复任何沿错误 $R_{\rm bad}$ 链得出的结论。不将原几何 D 的非零局部化换成范数单位。

## 7. 唯一实际执行

[冻结源](../notes/2026-11-28-unit211-Phi-zero-true-Bzero-whole-I6-twelve-by-two-8542.py)的 SHA256 为
`b802d6c9b7a46b544f1fd5f814b05337a552f938a660b8d047fe4e62ff4eae56`。唯一运行 46114522011 / job 140885249422 实际正常退出 0，用时 0.367564671 秒、峰值 41096 KiB；源限额为 120 秒、1 GiB。

其两个数学阶段分别在 0.218026、0.323905 秒返回，全头 Bézout、九个胶合条目、三条原规则、完整 I6 与全部系数分母均通过，精确除法乘回总数 430。stdout 4484 B，SHA256 为
`46cbe558fd948f9d5fb849760dc6c21e9975dcdfa7e8084fb8312cd399816e8f`。

源提交为 `4f576d7ee0e7d43a9f9e6fbc8f33f934ea6ebe34`；实际执行前于 2026-11-28 05:59:35.050917 UTC 真 pull 到 `c376ccf9cd92f7ff5ed5d17b24bf19a89fd8bd2b`，两 README blob 无变化。较早派发因工作流名大小写校验而被阻止的过程没有启动数学，不计为本源的数学运行；此前 selected-chart 源末 JSON 失败也没有重跑。

[小回执](../notes/2026-11-28-unit211-Phi-zero-true-Bzero-whole-I6-twelve-by-two-8542-execution.json)保留全部真实次数、来源身份及边界，不存可重算大系数。
