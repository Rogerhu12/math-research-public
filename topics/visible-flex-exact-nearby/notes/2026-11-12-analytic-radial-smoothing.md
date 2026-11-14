# 同一有限幅图的解析径向平滑与精确反射选项

状态：**已给显式解析函数定义、全核心二jet差及任意高jet预算；
这不是新的Newton解，也不是已完成的径向等距方程或闭帽。**

输入仍是 `phase_ring_continuation/type_fixed_step02.npz`，SHA256
`05d3e59cf338c5d2a2bde13aad7bf1d4e5247c326efb46b3148793e75a7ea883`。
本记录不改这个检查点，也不把其旧返回数自动转授给平滑后的新对象。
所有下面的差都针对同一批已保存 spline 系数，不重新拟合近似曲线。

## 1. 精确实数输入与原高度实现的微小区别

物理相位为 $\beta_j=a_{\rm ref}^3b_j$、
$\gamma_j=a_{\rm ref}^2c_j$，实际周长半径 $a$ 包括三个 mean 和
保存的 `radius_shift`。原高度求值器保存了浮点反导函数系数和另一个
浮点 slope spline；把两组系数都解释成精确实数时，两者不是代数上
完全相等的导数关系。

本记录选择明确的精确高度

$$
Z(x)=\int_0^x z_{\rm slope}(s)\,ds,
$$

其中 slope 的各项系数及三个 mean 组合均完整保存。原浮点反导函数
与这个积分的差，通过区间de Boor在0处的值、导数控制系数差及其
导数，得到核心 $|x|\le.6$ 上的上界

$$
(\|\delta Z\|,\|\delta Z'\|,\|\delta Z''\|)
\le(1.016\cdot10^{-13},1.597\cdot10^{-13},1.678\cdot10^{-10}).
$$

这些费用已经加入后面的几何差。没有把普通舍入量默认为严格零。

## 2. 紧支输入及全局五阶范数

取精确偶函数$\chi$：$|x|\le1$时为1，$|x|\ge2$时为0，
在$1<|x|<2$令$t=|x|-1$，

$$
\chi(x)=1-126t^5+420t^6-540t^7+315t^8-70t^9.
$$

其Bernstein控制系数是五个1后接五个0，端点的一至四阶导数为零。
所以$\chi\in C^4\cap W^{5,\infty}$。用Bernstein差分给各阶绝对上界

$$
(C_0,C_1,C_2,C_3,C_4,C_5)=(1,9,72,1008,9072,90720).
$$

对每一个物理相位系数、实际$a$和上述$Z$，定义紧支源$f=\chi f_0$。
原 quintic spline 是$C^4\cap W^{5,\infty}$，乘积仍属该空间。
程序合并正负两侧所有knots以及$\pm1,\pm2,\pm.6$，共1944个单元，
直接覆盖$[-2,2]$；不利用近似径向反射把正侧界复制到负侧。
每个导数用B-spline凸包及Leibniz乘积上界计算。

所得全局范数$M_j\ge\|f^{(j)}\|_\infty$包括：

| $j$ | 周长半径源 | 高度源 | 所有$\beta_j,\gamma_j$源的范数之和 |
| --- | ---: | ---: | ---: |
| 0 | 1.123817 | 2.509810 | .525726 |
| 1 | 5.286799 | 22.588299 | 3.649461 |
| 2 | 60.759323 | 180.706636 | 159.375880 |
| 3 | 848.464828 | 2529.895454 | 27687.891388 |
| 4 | 31722.875632 | 22769.158029 | 6902996.006 |
| 5 | 9512927.283 | 227693.485 | 2252032875.816 |

逐模的完整值在JSON中；表格向上取整。这里的高导数确实很大，不能
只凭$C^2$平滑误差小就授予canonical正常形所需的小常数。

## 3. 消二次矩的Gaussian组合

令$G_h$为方差$h^2$的中心Gaussian核，定义

$$
\mathcal S_h f=\frac{4G_h*f-G_{2h}*f}{3}.
$$

它的质量为1，一、二、三次矩为零。紧支$L^\infty$输入与Gaussian
卷积是整函数，所以这里每一个平滑后的标量系数都在复$x$上解析。
对$f\in W^{5,\infty}$，Taylor积分余项和核的绝对矩直接给

$$
\begin{aligned}
\|\mathcal S_hf-f\|_\infty&\le\tfrac56h^4M_4,\\
\|(\mathcal S_hf-f)'\|_\infty&\le\tfrac56h^4M_5,\\
\|(\mathcal S_hf-f)''\|_\infty&\le\tfrac{16}{15}h^3M_5.
\end{aligned}
$$

证明：前两式用三阶Taylor多项式及四阶余项；
$\int |(4G_h-G_{2h})/3|\,|x|^4dx\le20h^4$。
第三式对$f''$用二阶Taylor多项式，余项不超过$M_5|x|^3/6$；
相应绝对三次矩不超过$4h^3\mathbb E|N(0,1)|^3$。
$\mathbb E|N|^3=2\sqrt{2/\pi}<8/5$，故得到$16/15$。
这些是全实轴一致界，不是卷积积分的采样估计。

为严格恢复原振幅$\beta_4(0)$，只给平滑后的第一$\beta$系数加

$$
c_h e^{-4x^2},\qquad
c_h=\beta_4(0)-(\mathcal S_h(\chi\beta_4))(0).
$$

$|c_h|$由第一式界住，而$e^{-4x^2}$的零、一、二阶绝对上界可取
$(1,2,8)$。因此没有留下待解的振幅误差。下面$h=10^{-5}$表示JSON
所保存的那个精确二进制实数；不把十进制显示和二进制输入混作额外
未经计费的转换。

## 4. 真实R33曲面的二jet差

令$u,u_x,u_{xx},u_\theta$分别界相位变化$\delta\beta,\delta\gamma$
两者绝对值和及所标导数，$s_x,s_{xx},s_\theta$为原相位对应上界。
单位切向量对两个实相位的各偏导范数至三阶不超过1，于是

$$
\begin{aligned}
|\delta T|&\le u,\\
|\delta T_x|&\le u_x+s_xu,\\
|\delta T_{xx}|&\le u_{xx}+(2s_x+u_x)u_x+(s_{xx}+s_x^2)u,\\
|\delta T_\theta|&\le u_\theta+(1+s_\theta)u.
\end{aligned}
$$

零均值原函数的周期积分核给
$\|P_\theta\|_{L^\infty\to L^\infty}\le\pi/2<11/7$。
将这些界代入同一个$F=aP_\theta T+Ze_z$的Leibniz公式，即得完整
Cartesian二jet差。程序没有把独立$T$ jet当成截断原函数的实际导数。

不额外对称化时，$|x|\le.6$、全角圈的向上取整结果为：

| $h$ | $F$ | $F_x$ | $F_\theta$ | $F_{xx}$ | $F_{x\theta}$ | $F_{\theta\theta}$ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| $10^{-4}$ | 1.032e-9 | 3.367e-7 | 6.550e-10 | .004262 | 2.143e-7 | 4.980e-8 |
| $3\cdot10^{-5}$ | 8.454e-12 | 2.728e-9 | 5.306e-12 | .000115000 | 1.736e-9 | 4.034e-10 |
| $10^{-5}$ | 2.047e-13 | 3.383e-11 | 6.550e-14 | 4.259e-6 | 2.143e-11 | 4.980e-12 |

最后一行$|c_h|\le5.209\cdot10^{-16}$。这些界比较无限R33图；若基准
使用Q256有限原函数，还应加入uniform-phase-primitive-tail笔记的
六个角尾/混叠界，最大1.130e-10。实际浮点三角/FFT计算的舍入仍另计。

## 5. 精确径向反射的可选对象及其费用

原二进制knots最大反射缺陷1.7763568394002505e-15，最小正间距
大于.004525958071844305。因此原raw控制系数的符号复制不授予
整个spline精确径向偶奇性。另定义显式对称化源：

$$
a^+=\frac{a(x)+a(-x)}2,\quad
\beta_j^+=\frac{\beta_j(x)+\beta_j(-x)}2,\qquad
Z^-=\frac{Z(x)-Z(-x)}2,\quad
\gamma_j^-=\frac{\gamma_j(x)-\gamma_j(-x)}2.
$$

先作这个操作，再乘同一偶cutoff、作同一$\mathcal S_h$并恢复振幅。
Gaussian组合为偶核；$\beta_4^+(0)=\beta_4(0)$且卷积的奇部在0处为零，
所以同样的$c_h$预算仍成立。这个可选对象才有精确偶奇性；所有相应
零jet/奇偶jet匹配都由公式成立，而不是由于测试显示约$10^{-15}$。

反射缺陷的控制系数比较也包含knot移动。简述其可核机制：把反射
spline写成$\widetilde t_i=-t_{N-i}$和带相应符号的倒序控制系数。
导数控制系数差递推用

$$
\delta c_i^{\rm new}\le k\left[
\frac{\delta c_i+\delta c_{i+1}}{d_i}
+\frac{|\widetilde c_{i+1}-\widetilde c_i|\,|D_i-\widetilde D_i|}{d_i^2}
\right],\qquad d_i\le\min(D_i,\widetilde D_i).
$$

同一span内的de Boor每一层中，插值权的变化不超过$\delta t/h_{\min}$，
所以再付“层数×该变化×参考控制系数范围”。若$x$落在原knot与反射
knot之间，移动不超过$\delta t$即可到共同span，再付两函数的一阶
导数界乘位移。由于$4\delta t<h_{\min}$且所比较导数至二阶连续，
这覆盖了所有小的交错单元。knot差用精确有理数相减，所有随后基本
运算向外扩。物理相位乘积及cutoff按Leibniz继续传播。

紧支源的全局反射缺陷（尚未除以2）得到：

| 源 | $C^0$缺陷 | 一阶缺陷 | 二阶缺陷 |
| --- | ---: | ---: | ---: |
| 所有相位绝对值和 | 1.265e-12 | 3.074e-11 | 2.141e-9 |
| 实际周长半径 | 1.291e-15 | 9.357e-13 | 7.536e-10 |
| 精确积分高度 | 2.497e-15 | 2.372e-14 | 1.091e-12 |

对称化改变源至多为各缺陷的一半，其五阶范数仍不超过原全局$M_j$。
将此费用加入上一节后，**精确反射且解析**的$h=10^{-5}$新图与原输入的
全核心差可取

$$
(e_F,e_x,e_\theta,e_{xx},e_{x\theta},e_{\theta\theta})
\le(1.324\cdot10^{-12},6.604\cdot10^{-11},7.769\cdot10^{-13},
4.262\cdot10^{-6},4.192\cdot10^{-11},2.178\cdot10^{-11}).
$$

核的实现另外以显著不对称knots、精确对称控制系数以及跨越每个
交错knot间隙的网格核查；各阶观测差不超过给定上界的1.34%。这只是
实现检查，上面的控制系数/de Boor比较才是界的依据。

## 6. 解析带及任意高jet

对$|\operatorname{Im}x|\le h$，Gaussian绝对值直接给

$$
|\mathcal S_h f^{(j)}(x)|
\le\frac{4e^{1/2}+e^{1/8}}3 M_j<3M_j\quad(0\le j\le5).
$$

因此对$r\ge5$，实轴上的标量高jet可取

$$
\|f_h^{(r)}\|_\infty\le
\frac{3M_5(r-5)!}{h^{r-5}}.
$$

对恢复振幅的Gaussian项另加$3|c_h|r!2^r$即可。对称化源不会增大
这里的$M_j$。角strip仍由逐模$\cosh(4j\sigma)$加权计算；在
$|\operatorname{Im}x|\le10^{-5}$、$|\operatorname{Im}\theta|\le.02$上，
完整位置函数范数小于76.383。因此所有混合高jet有明确上界

$$
\|\partial_x^r\partial_\theta^sF_h\|_\infty
\le\frac{76.383\,r!s!}{h^r(.02)^s}.
$$

角带.04也可用，位置范数上界167.575。这支付了一个实际解析径向对象
及其高jet输入，不表示这些很大的常数已经使R39正常形或实际全传递
的迭代门闭合。旧返回图、低阶相位与边界反馈仍须针对新对象重算，
或用足够阶的误差稳定性转移；不能仅凭$C^2$差小跳过这一步。

## 7. 文件及从冻结输入重做

输入：`data/phase_ring_continuation/type_fixed_step02_analytic_smoothing_inputs.npz`，
389654字节，SHA256
`bd9b4d14b104183f80feaeea4c4c1a5d8c40b511bd58974dbca1bda842474532`。
其中完整保存相位/base/mean/shift的knots与系数、各高度slope及浮点
反导函数常数；后续从它重做，不需要再次生成背景ODE或样条拟合。
完整报告为同目录 `type_fixed_step02_analytic_smoothing_budget.json`。

脚本 `fourfold_phase_smoothing_budget.py` SHA256：
`462081a5829f17e9788a8ff26e149d58962ed42c2dd38bdea8d92ae1065d6477`。
其向外算术依赖沿用uniform-tail脚本和有理指数核，哈希在JSON中。

```bash
mkdir -p /tmp/visible-exact-smoothing
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python topics/visible-flex-exact-nearby/scripts/fourfold_phase_smoothing_budget.py \
  topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02.npz \
  --frozen-inputs topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_analytic_smoothing_inputs.npz \
  --core .6 --widths 1e-3 3e-4 1e-4 3e-5 1e-5 \
  --snapshot /tmp/visible-exact-smoothing/inputs.npz \
  --out /tmp/visible-exact-smoothing/report.json
```

该命令只产生范数与解析函数的明确定义，不写回主检查点，不新增
Newton状态，不把平滑后的未解径向方程或非固定Gaussian尾当成闭帽。
