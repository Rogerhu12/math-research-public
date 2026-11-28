# R150：W 原均值六行的实际返回、整个纯权 f 头支付与同点 f 唯一消去

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

**结论。** 在本文沿用的互异两值、物理 $D\ne0$ 的当前 W 原图上，真正原四式 $I_4=(E_1,E_{Be},E_{Bo},N_1)$ 给出全图首一 $f$ 二次和完整六行两列呈示。本次新纯权一次关系的头，完整 QQ 分解后仅含既有原单位与 $(2e+1)G_{36}$。后两因子分别由原 $J=Q$ 整支排除和整个 $G_{36}$ 原权曲线排除支付。因此当前整个 W 图有同一个唯一恢复
$$
f=-g(\lambda,T),\qquad \deg_{\lambda,T}g\le2,
$$
且 $I_4$ 精确化为该一次关系及四条纯 $(\lambda,T)$ 原条件。没有遗漏头零纤维，没有由 pair 或 norm 的必要性代替完整同点相容性。

首次运行实际还完成三条原 pair 三次和三个同 $f$ 范数四次。它们不证明 W 排空，也不产生新的有限点数界。本次运行没有构造 $N_S,P_S$；完整 $I_6/I_{11}$ 的后继仍须保留这些原条件。

## 1. 范围、定义及原来源

沿用[全图显式首一 f 二次与完整 I4／I6](R150-appendix-unit211-W-lambda-T-f-global-monic-f-two-and-exact-I4-I6.md)的当前 W 权环。特别是
$$
u=e+1,\quad Q=ek,\quad \overline V=uk+2,\quad
\ell=\frac{u((k+2)^2-2ek)}{k\overline V},\quad
\delta=1-Q,\quad m=u-\ell,\quad M=4bc\delta .
$$
$e,k,u,\overline V,\delta,M,m,P_{02},\Phi,\ell$ 等所用纯权分母有该原图的既有来源。本文不把互异值图的这些支付外推到 $h_U=k_U$ 碰撞图或 $\Phi=0$ 图。

本次源码自含，直接由真实四行 Gram、$\rho^2=\delta$ 的二次扩张和真正 dual 乘法构造原式。其乘法前两坐标是
$$
(v_0,v_1)(w_0,w_1)=(v_0w_0,v_0w_1+v_1w_0).
$$
singleton B 的完整均值保留 $2pr$。源码完整返回
$$
E_B=ap^2+2pr+ct^2
 -2(apu+pd_1+ru+ctY)-2X^2+4fX .
$$
$E_1$ 始终独立保留；没有将它替换成 weighted mean，也没有继承撤回的 derivative 平方公式。

同点原恢复为
$$
t=-\frac{P_f f+P_c}{bcQ\Phi},\quad
V=\frac{Jf-G+bcQt}{Q},\quad W_1=T_0/2+2uf,
$$
$$
x=\frac{(u-\ell Q)V-mW_1}{M},\qquad
y=\frac{\ell W_1-uV}{M}.
$$
其中 $G=\lambda P_{02}-(1-u)T_0$，
$P_c=QP_{02}(\ell+T)-GT_0$。原 $E_0,N_0,P$ jet 及权线性恢复的全部身份已在本次逐项返回。

## 2. 实际首一二次与完整六行

令
$$
\beta=2u-J/Q,\qquad
u-\beta=-\frac{ue(k+4)}{\overline V}=\frac{u\Phi}{2e}.
$$
它是现有纯权单位。实际构造
$$
q_f=\frac{bc}{2u(u-\beta)}
       \left(E_{Be}+\frac{\ell\delta}{m}E_{Bo}\right)
=f^2+q_1f+q_0,
\qquad
\deg_{\lambda,T}q_1\le1,\quad \deg_{\lambda,T}q_0\le2.
\tag{1}
$$
源码返回完整四原式乘子，也返回由 $q_f,E_{Bo}$ 反向恢复 $E_{Be}$ 的等式。

对 $F_i=E_1,E_{Bo},N_1$，令
$$
r_i=F_i-[f^2]F_i\,q_f=A_i+B_if.
\tag{2}
$$
则 $A_i$ 对 $(\lambda,T)$ 总次至多二，$B_i$ 至多一次。每条 (2) 的正反原身份和
$$
fr_i-B_iq_f=-q_0B_i+(A_i-q_1B_i)f
\tag{3}
$$
均已逐 $f$ 系数返回。

因此在首一二次环境中，原 $I_4$ 的完整关系模由六行
$$
(A_i,B_i),\qquad (-q_0B_i,A_i-q_1B_i)\quad (i=1,2,3)
\tag{4}
$$
生成。该二次环境以 $(1,f)$ 自由；进一步取原式商所得代数不被假设自由。六行实际完成于 0.831430965 秒。

## 3. 新纯权一次关系及内容零面的保留

把三个 $B_i$ 排成纯权系数矩阵
$$
\mathcal B_i=([1]B_i,[\lambda]B_i,[T]B_i).
$$
后两列的三个固定 cofactor $\mu_i$ 满足实际三个坐标身份
$$
\sum_i\mu_i B_i=\det\mathcal B,\qquad
\sum_i\mu_i r_i=(\det\mathcal B)f+\sum_i\mu_i A_i .
\tag{5}
$$

源码先对 (5) 的四个**实际原式乘子**共同清已付纯权分母，再精确除去这四个乘子的共同内容，并用约后的四乘子重新组合原式。其结果是
$$
hf+a(\lambda,T)=\sum_{j=1}^4\tau_j F_j,\qquad
F=(E_1,E_{Be},E_{Bo},N_1),\qquad \deg_{\lambda,T}a\le2.
\tag{6}
$$
整个 (6) 实际返回。这里没有把原方程除以未付内容；即使被约共同内容为零，右端仍是新的真实原组合，故该零面没有丢失。

约后的 $h$ 分母为非零有理常数，分子次数为 $(10,9)$、总次 17、54 项。只剥源码列出的旧权支持时，实际 gcd 层数为 $e:2,k:1,u:1$。其余纯权部分总次 13、次数 $(7,8)$、45 项，完整 QQ 因式恰为一次线性因子和一次 36 项因子。完整因子乘积已在运行中核回。

## 4. 两个剩余因子的精确识别及整头支付

本次输出没有大系数载荷。因子按源码固定编码
$$
\operatorname{JSON}([(\text{五变量指数},\text{有理系数字符串})]_{\text{指数升序}})
$$
记录规范 SHA256，变量次序为 $(e,k,\lambda,T,f)$。

线性因子的 37 字节规范定义正是 $2e+1$，SHA256 为
80a26dd535f6878afb58433c784fbf2fc63ab89f584fb6e65e0146f9dd877da1。
其支付来自[整个 J=Q 原排除](R150-appendix-unit211-general-J-equals-Q-complete-original-exclusion.md)与直接权恒等式
$$
(J-Q)\overline V=-2e^2k(2e+1).
\tag{7}
$$

36 项因子不是按次数猜测。直接读取既刊
[整个 G36 原源](../notes/2026-11-27-unit211-W-G36-whole-Q-six-original-thirty-six-column-return-8542.py)
中固定的 GDATA 定义。该原源完整 Git blob 为
c489948be8e967575417a1e21de51cd5a915dc80，
SHA256 为
3ec9b206da1dbde4103ebf7633e725e4cf5b8518055ac8f0945d7ba6a1e24a22。
将每条原定义 $(i,j,c)$ 改写成 $((i,j,0,0,0),c)$，按指数排序并使用与本次源码相同的紧凑 JSON 编码，得到 735 字节，SHA256 为
994fe0821fb8c70e7f82edf8aea19a17ee1ffa99fd5fd4b5b3c065daea84ad78。
它与本次实际完整 QQ 因子的规范 SHA256 完全相同，比例为 $1$。这是已保存定义的静态识别，没有重跑任何 G36 泛型或有限纤维门。

[整个 G36 原权曲线排除与全域恢复](R150-appendix-unit211-W-G36-entire-original-exclusion-and-global-F-recovery.md)的适用域正是本文的当前 W 图。该定理覆盖完整 1198 次有限参数支持、高 1134 次与全部低纤维，故这里可支付整个 $G_{36}$，不把函数域泛型返回外推成整曲线排除。

因此，存在非零有理常数 $c$ 使
$$
h=c\,e^2ku(2e+1)G_{36};
\tag{8}
$$
对支付而言 (8) 的有理常数无关。所有因子现均为本图已有单位，整个 $h=0$ 原域已经由既有完整结论覆盖。没有新加权开图条件。

**执行状态与推论须分开。** 冻结源码的有限 paid 表没有列入 $(2e+1)$ 和 $G_{36}$，所以实际日志准确记录 fullHeadIsAlreadyPaid=false，没有执行其可选 $f=-g$ 展开分支。本文第 4 节是对实际因子与既刊原定理的识别；下面的结论由已经返回的 (6) 作合法代数推导，不伪称该可选分支已执行，也不为它新增重跑门。

## 5. 整个当前 W 的精确同点消元

令
$$
g=a/h,\qquad R=f+g.
$$
由 (6)、(8)，$R\in I_4$，且 $g$ 的系数只有已付纯权分母，$\deg_{\lambda,T}g\le2$。原点上的 $f$ 唯一为 $-g$。

还必须保留
$$
P_0=g^2-q_1g+q_0,\qquad
P_i=A_i-B_i g\quad(i=1,2,3).
\tag{9}
$$
准确双向等式为
$$
q_f=(f+q_1-g)R+P_0,\qquad
r_i=B_iR+P_i.
\tag{10}
$$
结合原正反变换，得到整个当前权环上的理想等式
$$
I_4=(R,P_0,P_1,P_2,P_3).
\tag{11}
$$
其中 $\deg_{\lambda,T}P_0\le4$、$\deg_{\lambda,T}P_i\le3$。这是同一个 $f$ 的恢复及完整原均值条件，不是分别选择三个二次根。它也不意味着任意 $(\lambda,T)$ 满足六个必要标量就满足全部原系统。

完整 $N_S,P_S$ 仍须与 (11) 同点返回。将它们先对首一 $q_f$ 短除、再用同一个 $f=-g$，可以精确保持原 $I_6$；本次未执行这些后继运算，不在本稿添加其实际系数、结果式或空性宣称。

## 6. 六条新的纯值坐标必要式

本次实际还返回
$$
C_{ij}=B_jr_i-B_ir_j=A_iB_j-A_jB_i,
\tag{12}
$$
以及
$$
N_i=(A_i-q_1B_i-B_if)r_i+B_i^2q_f
=A_i^2-q_1A_iB_i+q_0B_i^2.
\tag{13}
$$
每条目标均在四个真实原乘子共同约内容后重新完整返回，并只剥已付纯权支持。几何头、共同几何零面和所有未付权因子都保留。

| 实际必要式 | 分子次数 $(e,k,\lambda,T)$ | 总次 | 项数 |
| --- | --- | ---: | ---: |
| pair $E_1,E_{Bo}$ | $(13,17,3,3)$ | 25 | 1378 |
| pair $E_1,N_1$ | $(14,19,3,3)$ | 28 | 1668 |
| pair $E_{Bo},N_1$ | $(17,23,3,3)$ | 33 | 2483 |
| 同 f norm $E_1$ | $(16,22,4,4)$ | 33 | 3278 |
| 同 f norm $E_{Bo}$ | $(21,27,4,4)$ | 39 | 5203 |
| 同 f norm $N_1$ | $(18,25,4,4)$ | 36 | 3992 |

(12) 对 $(\lambda,T)$ 总次至多三，(13) 至多四。表中大系数不另存缓存；其精确定义、字节数与规范 SHA 在小回执中。三 pair 加三 norm 本身未被宣称充分、互素或排空。

## 7. 真实执行与保存边界

唯一正常数学运行：

- run 46132364167，job 140940115528。
- source commit 6a4c3649fba8e7259c9672f88c10ff6d1c7dc7b0。
- 源 blob b1d80b4b8d57b78062148315c16dc665a8224d22，SHA256 f6d0afca90813e795bb67c80ba7906d3075e8e44e4875b73302de2f19a14825b。
- 内层 exit 0；驱动 2.732694879 秒；子进程最大 RSS 49112 KiB。
- 最后数学 checkpoint 2.655064521 秒。
- stdout 13392 字节；SHA256 666d06c00b7d346869f9dbce2184c686e46acdc15120a16ba4c9c628002d05e7。
- 实际 592 次精确多项式除法乘回、37 次原 f 系数返回、508 次已付支持乘回、6 次四源内容约除、3 次同 f 范数身份；69 个不同纯权分母全部检查。

真实 pull 于 2026-11-28 09:51:01.162026 UTC 从 source commit 更新到 56c35c4ca2d36e03831702cf1a4a1ba9ebb8efeb，两 README 未变。根 README blob 为 99c5ad8d06e939e6cfbbab1afdeffa5463f15f18。

此前 workflow 46132152322 / job 140939466184 被驱动中旧 README 基准在数学 Popen 之前拦下；没有源执行和科学回执。上列是更新已读规则基准后的首次数学运行，不是数学门重放。原 d21 输入未派发，也不记为失败。

规范源：
[首次完整源](../notes/2026-11-28-unit211-W-lambda-T-f-original-monic-two-pure-weight-head-and-scalars-8542.py)，
[输入说明](../notes/2026-11-28-unit211-W-lambda-T-f-original-monic-two-pure-weight-head-and-scalars-8542-input.md)，
[小回执](../notes/2026-11-28-unit211-W-lambda-T-f-original-monic-two-paid-head-and-scalars-receipt-8542.json)。

本稿仅把实际完成的原均值接口、全头支付和同点唯一恢复登记。原 W 剩余方程继续，未宣称普通 Hilbert ISP 完成。
