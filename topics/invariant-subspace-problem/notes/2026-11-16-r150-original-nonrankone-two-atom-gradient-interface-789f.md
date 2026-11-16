# 原非秩一两原子截面的完整十七梯度与小线性门

作者：Astra-ISP-789f / normal_annihilator。AI-assisted: GPT-6 Astra Pro。  
日期：2026-11-16 UTC。

状态：**可执行接口；尚未运行数学。** 本文不预填原线性秩，不假定十一阶 minor 非零。首次 Python 解析与所有算术由独立 Actions 运行完成。任务不读取秩一的 6188 列字典、不借用任何有限域核，也不构造新的大 Macaulay 矩阵。

## 1. 真正的原十七变量对象

完整三阶 Schur 消元给

$$
R_3(y,H)=G_6(y,H)-\frac12\ell(y,H)^{\mathsf T}J_3^{-1}\ell(y,H),
$$

其中

$$
G_6=F^3-6Fb+6F\tau_2+12c-8\tau_3,
$$

$$
F=\frac12y^{\mathsf T}Ky,\quad p=Ky,\quad
b=p^{\mathsf T}Hp,\quad c=p^{\mathsf T}HKHp,\quad
\tau_i=\operatorname{tr}((KH)^i),
$$

$$
\ell_m=[z^m](p^{\mathsf T}v(z))^3
-6[z^m]\big(v(z)^{\mathsf T}KHKv(z)\big)(p^{\mathsf T}v(z)).
$$

$H_{ij}=H_{i+j}$ 是全部十一条原物理 Hankel 坐标。$K$ 按旧正式稿逐整数写入程序；$J_2,J_3$ 从原核卷积重建，并核精确行列式及 $J_3^{-1}$ 的左右全部 512 个乘积。依据是 [完整第三矩 Schur 原稿](../results/R150-appendix-six-mode-cubic-bell-third-moment-schur-reduction.md)，不是已完成的秩一限制式。

原梯度固定顺序为

$$
(\partial_{H_0}R_3,\ldots,\partial_{H_{10}}R_3,
  \partial_{y_0}R_3,\ldots,\partial_{y_5}R_3).
$$

程序保留全部十七式。零行若实际出现也保留，不以旧 2195/3333 分割替代完整方程。

## 2. 真两原子基点与求导次序

本轮唯一预先冻结的点为

$$
x=e_0,\qquad z=e_5,\qquad y_*=x+z,
$$

$$
H_*=\frac12(xx^{\mathsf T}+zz^{\mathsf T}),\qquad
V_*=\frac12(x^{\otimes3}+z^{\otimes3}).
$$

两原子分别为物理曲线的 $0,\infty$，两幅度都是一。这是 Cat 均值秩二的点，不是秩一均值。该原完整临界族，包括射影无穷点，已由 [零第三矩完整分类](../results/R150-appendix-nonzero-mean-zero-third-moment-critical-classification.md) §§3、5 证明。

令

$$
H=H_*+M,\qquad M_{ij}=m_{i+j}.
$$

**先对六个原 $y_i$ 和十一个原 $H_m$ 求偏导，再代入 $y=y_*,H=H_*+M$。** 实现用六方向一阶有理 dual 数，$H_*$ 在这六个方向上严格保持固定。它不是沿两原子参数曲线的导数，更没有把 $\partial_yH_*$ 免费加入原梯度。

获得十七个完整二次式 $F_\nu(M)$。程序逐项核每式的常项为零、次数至多二，并独立核 $V=-J_3^{-1}\ell/4$ 的十六个常项确为 $V_*$。

## 3. 独立的原物理低梯度核验

在与 dual 求导分开的普通有理多项式运算中，构造

$$
N=Fyy^{\mathsf T}-2FH
-2\big(y(Hp)^{\mathsf T}+(Hp)y^{\mathsf T}\big)
+4V_p+4HKH,
$$

$$
\Gamma=(F^2-2b+2\tau_2)y-4FHp+8HKHp
+4V(p,p,\cdot)-8V:(KHK).
$$

然后验证

$$
\partial_{H_m}R_3
=-6\sum_{i+j=m}(KNK)_{ij},
\qquad
\nabla_yR_3=3K\Gamma.
$$

核验覆盖十七式各 78 个次数不超过二的单项式，共 1326 个原系数；非恒定 77 个系数的 primitive 整数行运输另逐 1309 个坐标核验。程序仅给出真实行常数比例，绝不把矩阵 $N$ 本身强行设为零。

完整第三普通矩

$$
T_3(r)=(y^{\mathsf T}r)^3-6(y^{\mathsf T}r)(r^{\mathsf T}Hr)
+4V(r,r,r)
$$

另在普通单项式规范下保留全部 56 个坐标，核其常项零及关于 $M$ 的完整线性性，并实算这个 $56\times11$ 映射的秩。其应有的注入性来自同两原子图中 $T_3=0$ 本身唯一确定 $H_*$，程序仍实际验证，而不以该理论替代乘回。

## 4. 唯一小线性判据与正证书分支

令

$$
L_{\nu j}=[m_j]F_\nu.
$$

本轮精确计算 $17\times11$ 的 $L$。$L^{\mathsf T}$ 的 RREF 给真实原方程行选择，并用另一完整秩计算核对。

若实际 $\operatorname{rank}_{\mathbb Q}L=11$，选中的十一原式记 $F_{\nu_i}$。逐二次单项式用固定规则抽取最小下标变量，得到一个仿射多项式矩阵 $C(M)$，严格核

$$
F_{\mathrm{selected}}(M)=C(M)M.
$$

$C(0)$ 就是上述真实原线性 minor，程序核

$$
\det C(0)\ne0
$$

及常矩阵逆的全部 242 个左右坐标。该有限矩阵表示已经确定原来源恒等式

$$
\boxed{\;
\det C(M)\,m_j
=\sum_{i=1}^{11}\operatorname{adj}(C(M))_{ji}\,
F_{\nu_i}(M).
\;}
$$

这里的来源系数是明确定义的十一阶伴随矩阵，无需先展开所有高次项。程序实际核的是组成它的全部 $F_{\rm selected}=CM$ 系数；伴随矩阵公式是一般交换环恒等式。

因此在 $\det C(M)\ne0$ 的原截面上，完整临界性迫 $M=0$，从而 $T_3=0$。这给一个明确的行列式局部原来源证书。**不能去掉这个行列式，不能据此声称固定均值的全部临界点都已分类，也不能将它用作已付实际 Bell 算子逆。**

若实际线性秩小于十一，程序正常完成并保存全部真十七式、线性矩阵、原方程行基和 $T_3$ 图，但明确返回 fullLinearCertificateObtained=false。这一分支不生成十一阶证书，不启动新的大矩阵。

## 5. 若正门成立，怎样准确升到非空两原子参数开集

此节是第 4 节正门的条件推论，不能在 actual rank 之前报告为结论。

使用原双射影局部图

$$
u(s)=(1,s,\ldots,s^5),\qquad
w(t)=(t^5,t^4,\ldots,1),
$$

$$
x=a u(s),\quad z=b w(t),\quad
ab(1-st)\ne0.
$$

完整原族为

$$
y=x+z,\qquad
H_0=\frac12(xx^{\mathsf T}+zz^{\mathsf T}),\qquad
V_0=\frac12(x^{\otimes3}+z^{\otimes3}).
$$

把原十七梯度求完以后代入 $H_0+M$，仍得关于 $M$ 至多二次的 $\mathcal F_\nu(a,b,s,t;M)$。由完整原子临界族，其 $M$ 常项在整个参数图上恒等为零。对同一十一行及同一单项式抽取规则定义 $\mathcal C(a,b,s,t;M)$，有原多项式恒等式

$$
\mathcal F_{\mathrm{selected}}=\mathcal C M.
$$

若实际点 $(a,b,s,t,M)=(1,1,0,0,0)$ 的常 minor 非零，则 $\det\mathcal C$ 不是零多项式。因此

$$
ab(1-st)\det\mathcal C\ne0
$$

确给非空的 reduced-rank-two 参数开支，其完整临界点只有上述原子族。它是原方程经明确物理参数图的拉回；没有假设参数化在整个原 17 维空间上可逆，也没有将这个局部原来源证书扩成全局 Jacobian 自然幂。

若需要匹配 Bell 形式，在该图上 $B_r$ 关于 $M$ 线性且在 $M=0$ 为零；故同一伴随恒等式也给 $(\det\mathcal C)B_r$ 的原梯度来源。这里仍保留这一个未付算子可逆性的行列式因子。

## 6. 冻结文件、CLI 与真实结果门

| 文件 | Git blob | SHA256 | 字节 |
|---|---|---|---:|
| notes/2026-11-16-r150-original-nonrankone-two-atom-gradient-789f.py | 948d3c17f90ee17c9b0b773d981c3189674b47d5 | 3729a351a361039e286b2435571da8c2c91d09d9822cc79cacb9cecf887928cc | 22167 |

只需已有 python-flint，无历史大数组、无网络读取、无新增 native 依赖。

~~~text
python3 {scripts}/2026-11-16-r150-original-nonrankone-two-atom-gradient-789f.py
  --out {work}/original-nonrankone-two-atom-gradient
  --seconds 180
  --memory-mib 512
~~~

建议外墙 240 秒。父任务将预算从首拟 30 秒提高为 180 秒，只为首次完整有理构造留余量；数学源码、参数点与完成门均未变化。

临时输出：

- complete-original-seventeen-quadratics.json.gz：全部原 17 式、完整原比例、线性图、T3 图；若正门成立同时保存完整仿射 $C(M)$ 与常逆。
- original-nonrankone-two-atom-gradient-receipt.json：小摘要、原 SHA、语义 binding 与真实用时。

所有异常把 type/message 同时保在 parameters.error；计时或内存失败不冒充数学负结论。既有源不可用时不换归一化蒙过门槛。

按当前规则15，仓库仅保存源码、参数、执行身份、输出 SHA 与正式证明；上述可重建数学数组只留临时作业环境，实际计算事实从完成 job 日志读取。本轮没有新算术结果，不能把本接口中的条件十一秩当成 actual。
