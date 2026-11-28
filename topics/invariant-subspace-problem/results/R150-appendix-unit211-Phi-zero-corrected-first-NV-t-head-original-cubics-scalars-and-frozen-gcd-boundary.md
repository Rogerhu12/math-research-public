# 正确 Phi：完整 NV 第一 t 头支的原小三次、三个标量与冻结 gcd 边界

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / literature_deddens。日期：2026-11-29（Asia/Taipei）。

## 1. 已完成的原结论及本次边界

在当前正确 $\Phi=0$、distinct singleton、物理 $D_{\rm phys}\ne0$ 原图，完整 NV 的第一个 t 首项零支
$$
T+u\sigma=0
\tag{1}
$$
具有下文的准确原二次、三次和完整 NV 小三次。首次运行已完整返回该恢复、两次首一 lambda 短除和三个原标量：
$$
n_H(u,Q,\sigma)=0,\qquad
c_{H,V}(u,Q,\sigma)=0,\qquad
n_V(u,Q,\sigma)=0.
\tag{2}
$$
三个实际分子的 $(u,Q,\sigma)$ 次数分别为
$$
(6,3,6),\qquad (8,4,5),\qquad (12,7,6),
$$
总次数分别为 $12,13,18$。

其后的唯一 $\mathbb Q(u,Q)[\sigma]$ gcd 目标触及预定 $120$ 秒资源截止。只返回首个种子 nH 的首一化；第一次合并 gcd 未返回，最终三个原式乘子及纯权 cover 也未返回。因此本文没有取得整 (1) 支排除、纯权支持或新点数界。

唯一实际为 [run 46166961445](https://github.com/Rogerhu12/math-research-public/actions/runs/46166961445)，job 141046534179。内层退出码为 $-14$，实际耗时 $120.073936225$ 秒。整个三标量 gcd 目标冻结，不以加时、改序、续轮或换算法方式重播。

## 2. 原坐标、完整矩与唯一首一 lambda 二次

仍记
$$
s=u-1,\quad \delta=1-Q,\quad
L=Q-2(u-1)(u-2),\quad \ell=L/Q,\quad m=u-\ell,
$$
$$
M=\ell(2u-\ell Q)-u^2=4bc\delta,\quad M_n=QM,
$$
$$
T_0=2u-\ell Q-2u^2=-Q-4s,\quad
J=2u(1-u)+\ell Q,\quad J-Q=-4s^2,\quad P_{02}=2s\ell Q.
$$
只使用当前旧已付纯权
$$
uQ\delta s(Q+4s)L M_n(2\ell-1)
$$
及正确原等权审计支付的 m 分子。没有沿撤回的 wrong-Rbar 链恢复任何单位。

本支取 $T=-u\sigma$，按[正确整个 t 参数原恢复](R150-appendix-unit211-Phi-zero-corrected-whole-t-parameter-three-mean-generators-and-monic-lambda-cubic.md)，
$$
E=\frac{P_{02}(T+\ell)}{T_0},\qquad
f=\frac{P_{02}\lambda-QE+sT_0}{J-Q},\qquad
\mathcal V=f+bc\,t-E,
$$
$$
A_1=2E,\qquad W_1=T_0/2+2uf,\qquad
w=\lambda-1+u\sigma.
\tag{3}
$$
因此 f 对 $(\lambda,\sigma)$ 仿射，与 t 无关。原 $x,y$ 及四阶 Gram 仍由
$$
x=\frac{(u-\ell Q)\mathcal V-mW_1}{M},\qquad
y=\frac{\ell W_1-u\mathcal V}{M}
$$
恢复。源保真实 double-germ 乘法
$(vz)_1=v_0z_1+v_1z_0$。

原 singleton 比值完整变成
$$
h=1-p\sigma,\qquad k=1-q\sigma,\qquad
p=1+\rho,\quad q=1-\rho,\quad \rho^2=\delta.
\tag{4}
$$
所有量来自同一个 sigma，不选单根。设
$$
A_\lambda=2\lambda^2-2\lambda+1,\quad
B_\lambda=4\lambda^3-6\lambda^2+3\lambda-1,\quad
V_2=2u-\ell Q,\quad V_3=2V_2-uQ.
$$
两个原移位矩严格等于
$$
E_2=V_2\sigma^2-A_\lambda,\qquad
E_3=-V_3\sigma^3-B_\lambda .
\tag{5}
$$
于是有真正首一二次
$$
\boxed{
q_\lambda=\lambda^2-\lambda+\frac{1-V_2\sigma^2}{2}
=-\frac12E_2.
}
\tag{6}
$$
这里没有倒 $V_2,V_3,\sigma,D$ 或新的 lambda 头。完整二次结构和所有降头面都保留。

## 3. 完整原 NV 的小三次

令 $\mathbf1=(1,0,1,1)$、$g_0=(0,0,p,q)$、$e_1=(0,1,0,0)$。由 (4)，实际原向量满足
$$
\mathbf V=(1,w,h,k)=\mathbf1-\sigma g_0+w e_1.
\tag{7}
$$
本节 N 表示**未乘 ell 平方**的完整原值 $N_4(\mathbf V)$。令
$$
\mathcal E_0=2W_1-T_0-4uf,\qquad
n_0=N_4(g_0)-2\lambda P_{02}.
$$
真正 dual Gram 的完整二次型给
$$
\begin{aligned}
N_4(e_1)&=4(f-u),\\
\operatorname{Pol}_{N_4}(\mathbf1,e_1)&=2(u-2f),\\
\operatorname{Pol}_{N_4}(\mathbf1,g_0)&=T_0+\mathcal E_0,\\
\operatorname{Pol}_{N_4}(g_0,e_1)&=-2\mathcal E_0 .
\end{aligned}
\tag{8}
$$
因此 (7) 展开为完整原身份
$$
\begin{aligned}
N={}&2\lambda P_{02}\sigma^2+4(f-u)w^2-T_0\sigma+2(u-2f)w\\
 &+\sigma^2n_0+(2\sigma w-\sigma)\mathcal E_0 .
\end{aligned}
\tag{9}
$$
源从原 Gram 直接返回 (8)、原 E0/N0/P1 恢复和完整 N4。由 (3)，$\mathcal E_0=n_0=0$，所以
$$
\boxed{
N=2\lambda P_{02}\sigma^2+4(f-u)w^2-T_0\sigma+2(u-2f)w.
}
\tag{10}
$$
(10) 是不含 t 的三次式，未施加物理 $t=0$，也未用 NV 的部分替代全值。

实际 N 分子关于 $(u,Q,\lambda,\sigma,t)$ 次数为 $(6,2,3,3,0)$、总次数 $9$、$90$ 项；分母仅旧已付权，次数为 $(2,1,0,0,0)$、总次数 $2$、$5$ 项。分子 profile SHA256 为

    3f1d658e166c11e52ee824d4cb8a67d687181d416c4cdbc36a87abf6cf941284

完整原图及 (5)–(10) 在实际数学时间 $0.136771299$ 秒全部返回。

## 4. 两次首一短除与三个新原标量

只用 (6) 作 lambda 首一除法。第三矩的完整余式可以直接写成
$$
E_3=a_H+b_H\lambda+Q_Hq_\lambda,
$$
$$
a_H=\sigma^2(V_2-V_3\sigma),\qquad
b_H=1-2V_2\sigma^2,\qquad Q_H=-4\lambda+2 .
\tag{11}
$$
对完整 (10) 同样有
$$
N=a_V+b_V\lambda+Q_Vq_\lambda .
\tag{12}
$$
(12) 的 $a_V,b_V,Q_V$ 由首一普通短除唯一确定；两条完整普通原多项式身份都已实际返回。没有倒 $b_H,b_V$ 或某个新的 value 头。

写 $q_\lambda=\lambda^2+q_1\lambda+q_0$，取
$$
p_H=a_H-q_1b_H-b_H\lambda,\qquad
p_V=a_V-q_1b_V-b_V\lambda.
$$
三个新必要标量和全部三个原式来源为
$$
\begin{aligned}
n_H&=a_H^2-q_1a_Hb_H+q_0b_H^2\\
   &=p_HE_3+(b_H^2-p_HQ_H)q_\lambda,\\
c_{H,V}&=a_Hb_V-a_Vb_H\\
   &=b_VE_3-b_HN+(b_HQ_V-b_VQ_H)q_\lambda,\\
n_V&=a_V^2-q_1a_Vb_V+q_0b_V^2\\
   &=p_VN+(b_V^2-p_VQ_V)q_\lambda .
\end{aligned}
\tag{13}
$$
实际三个身份都对完整 $(\lambda,\sigma)$ 多项式返回。因 $q_\lambda=-E_2/2$，它们就是原 E2、E3 与完整 NV 的组合。

例如若 $x_0=V_2\sigma^2,\ y_0=V_3\sigma^3$，(11) 还给
$$
2n_H=1-3x_0+6x_0^2-4x_0^3-2y_0+2y_0^2.
\tag{14}
$$
这只解释第一标量的短结构，不另执行系数展开。

实际数据如下。次数均为原分子次数，没有把纯权分母删作未知单位：

| 标量 | $(u,Q,\sigma)$ 次数 | 总次数 | 项数 | 完整原返回时刻 |
| --- | --- | --- | --- | --- |
| $n_H$ | $(6,3,6)$ | $12$ | $35$ | $0.145223930$ 秒 |
| $c_{H,V}$ | $(8,4,5)$ | $13$ | $108$ | $0.148783748$ 秒 |
| $n_V$ | $(12,7,6)$ | $18$ | $283$ | $0.157135951$ 秒 |

三个分子 profile SHA256 依次为

    3c3631c246fc7c5d23e2f974328843eee4999d2ce218e5d4d27c2d3d879ac9c5
    f887de52d6d48460ed55a8d051e9748cd574b528ce0f153df8162271ec26e7cd
    d1fb445a99a7256f80721e86552c3e2dff62f47c25acf8d7ea08692c5de8146d

$n_H$ 的分母是 1；另两分母的 $(u,Q)$ 次数为 $(2,1)$ 和 $(4,2)$，总次数为 $2$ 和 $4$，分别有 $5$ 和 $12$ 项，均已逐项确认只含旧已付权。独立范数为零未被当作完整同根充分性；原三个式子、所有其他原条件和重根结构均保留。

## 5. 唯一 gcd 未完成，准确冻结范围

预定顺序是 $(n_H,c_{H,V},n_V)$。实际只在 $0.162765288$ 秒返回 index 0：首个 nH 的首一 sigma 六次及其单种子来源。该日志中的 gcdDegree=6 只描述这一次初始化，**不是三式共同 gcd 的次数**。

之后直到源自身总 $120$ 秒 alarm 终止，没有首次两式合并 gcd 的返回，也没有以下任一结果：

- 三个标量的最终 Bézout 或共同 gcd；
- 将最终组合合回三个原分子的终端身份；
- 最终实际分母 LCM、纯权 cover 或其因式；
- 整第一头支排除、有限权点或有限规范点界。

驱动原回执的 stop_reason 字段为 null，source_exit_code 为 $-14$。结合源最初固定的 $120$ 秒 ITIMER_REAL 及完整日志，边界是 SIGALRM 截止；没有 Python 实现异常回溯，也没有内存触界。实际峰值 RSS 为 $130724$ KiB。此门已冻结，保留以上完整已返原结论，不继续其 gcd 轮、改序或换算法重播。

## 6. 精确来源与小回执

[唯一源](../notes/2026-11-28-unit211-Phi-zero-corrected-first-NV-t-head-original-moments-and-value-8542.py)、
[首次输入](../notes/2026-11-28-unit211-Phi-zero-corrected-first-NV-t-head-original-moments-and-value-8542-input.md)、
[实际小回执](../notes/2026-11-28-unit211-Phi-zero-corrected-first-NV-t-head-original-moments-and-value-8542-execution.json)。

源 Git blob：

    e362142779557f1aba8f349ac6c39b7135ab9acd

源 SHA256：

    05f9b72e900b1176ae1dc765786841fa01da8b6dc474ba407d52c3df7f3b4d89

输入 blob 为 124862062f733680ab436653deecfe696518fb2b。源零依赖，预算 $120$ 秒 / $1$ GiB，外层 $135$ 秒；未运行旧 Q 主分量、旧轴比较、已成加权投影或 b53 同 sigma 十次门。

| 实际项目 | 返回 |
| --- | --- |
| run / job | 46166961445 / 141046534179 |
| 源提交 | 39d21734df0bfa597288ae5e63735ecb814ad451 |
| 实际 pull 后提交 | d4bcf94bb6f3a793d3daeb5ac1e4a5d51787cc00 |
| 规则读取 UTC | 2026-11-28T16:47:01.286892+00:00，两份 README 未变 |
| 驱动耗时 / RSS / 内层退出码 | $120.073936225$ 秒 / $130724$ KiB / $-14$ |
| 最后完整数学记录 | index 0 单种子，$0.162765288$ 秒 |
| stdout | $8443$ B，七条数学记录 |

stdout SHA256：

    f048907b0dbce9a8945bd0767ff3f5ca18fb7bf277245d6cc0a9d23c957b7398

完整 (1) 支仍未排除。第二个 NV t 头支也未被本次测试。正确 Phi 的其他已刊有限生成和公共权曲线界不变，普通 ISP 仍未完成。
