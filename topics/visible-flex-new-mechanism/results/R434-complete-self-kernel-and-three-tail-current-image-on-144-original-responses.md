# R434：144 个原响应的完整 self 核与三个真实尾矩 current 的联合像

日期：2026-11-16。**唯一新原式计算已在本公开仓库 GitHub Actions 完成。** 本稿报告同一组原成本系数的完整 self 核和三个 current 联合像，保留原右锚、全部尾常数和每个 current 的全部十三坐标。计算没有评价任何具体 profile 或退化点，也没有证明全部原响应空间或实际几何控制像等于本有限模块。

## 1. 完成结果与准确范围

采用[已发表合同](../notes/complete-response-self-current-design-20261116.md)和[首次执行审源](../notes/complete-response-self-current-entry-review-20261116.md)中的原成本
$
B_{E,\tau}=\mathcal B_E\tau,\qquad
E\in(P,R,S,L,U,V,T,Y),
$
$
\tau\in(H_0,\ldots,H_6,J_0,J_1,J_2,
\chi_{30},\chi_{32},\chi_{34},\chi_{37},\chi_{40},
\chi_{100},\chi_{104},\chi_{109}).
$
144 是成本标签数，不预设它们作为原响应独立。系数顺序为 $\tau$ 在外、$E$ 在内。

令 $V=\mathbb Q^{144}$，令 $Q:V\to\mathscr Q$ 为完整 universal self 函数的已证忠实坐标，包括九个 ordered 矩阵坐标及完整 local Euler 多项式。令
$
\mathcal C:\ker Q\longrightarrow\mathbb Q^{39}
$
同时记录三个真实尾矩 $n_0,n_1,n_2$ 的完整 $\mathcal K/4$ current；三个矩必须使用**同一个** $z\in V$。

这次实际计算得到
$
\boxed{\operatorname{rank}Q=59,\qquad
\dim\ker Q=85,\qquad
\dim\mathcal C(\ker Q)=32.}
\tag{1}
$
其中 85 是系数关系空间的维数，不是未经商去重复后的几何控制维数。对这 85 个关系的 current 映射，系数核为 53；同样没有据此断言 53 个不同几何方向。

[R432](R432-complete-zero-order-kernel-and-all-degenerate-point-response-matrices.md) 已付的三个矩各七个 p-only 方向共 21 维，作为**共同提升**包含在(1)的像中。因此本有限原模块新增的含 $u$ 商像准确为
$
\boxed{32-21=11.}
\tag{2}
$
它既不是全部十八维，也不是下面三个孤立 MEMBER 坐标所组成的三维空间。

## 2. 保留完整原 current 的坐标约定

记 $u=u(x),p=u',r=u'',t=u'''$，
$
I(F)(x)=\int_{r_*}^{x}F,\qquad J=-I .
$
对于原 $\tau$，保其完整局部系数 $a_\tau,b_\tau,c_\tau$，并令
$
h_\tau=(a_\tau r)'+b_\tau p,\qquad h_\tau'=-c_\tau u.
$
对原 E8 算子的真实二次尾 $w=p_E(n)$，
$
\mathcal K_{\tau,w}
=2\{a_\tau(pw''-rw')+wh_\tau+uI(c_\tau w)\}.
\tag{3}
$
(3)的左值由真正外 profile 平端确定为零；内层 $w$ 和 $I(c_\tau w)$ 的左值没有重置。计算先对同一个原成本组合求和、保完整 locality，再在一个 $A_u=6pt-2r^2=0,\ p\ne0$ 点使用 $t=r^2/(3p)$。没有微分这个单点关系，也没有删去高阶 jet 或非局部残项。

采用 [R433](R433-actual-universal-ordered-flux-zero-and-explicit-local-cap-currents.md) 对 $\mathcal K/4$ 的十三坐标，每个尾矩依次为
$
(A_0,A_1,A_2,B_0,B_1,C_0,\ 
p^3,p^2r,xp^2r,pr^2,xpr^2,x^2pr^2,S_7),
$
$
S_7=2xp^3-5x^2p^2r+3x^3pr^2.
$
前三块分别对应 $n_0,n_1,n_2$，所以总坐标下标为 $13j+k$。六个含 $u$ 坐标采用 R433 的**完整 canonical representatives**，含其固定的 p-only 项；不能只保每个代表中的含 $u$ 单项重新解释系数。

为避免与实际尾矩或导数混淆，下文写 $A_\nu^{[j]},B_\nu^{[j]},C_0^{[j]}$，其中方括号 $j=0,1,2$ 只表示尾矩块。

## 3. 七条完整 annihilator，给出本模块的充要条件

原 stdout 给出七条完整 39 坐标 annihilator。翻译为上述人读记号，它们是
$
\begin{aligned}
C_0^{[0]}&=0,\\
C_0^{[1]}-2B_0^{[0]}&=0,\\
A_1^{[2]}+\tfrac12A_2^{[1]}&=0,\\
A_2^{[2]}&=0,\\
B_0^{[2]}+\tfrac12B_1^{[1]}-A_1^{[0]}&=0,\\
B_1^{[2]}-2A_1^{[1]}-A_2^{[0]}&=0,\\
C_0^{[2]}-2B_0^{[1]}-B_1^{[0]}&=0.
\end{aligned}
\tag{4}
$
所有 annihilator 都不接触 p-only 坐标；这与原 21 个共同提升完全一致。

七条关系线性独立，因为可分别解出不同的
$C_0^{[0]},C_0^{[1]},A_1^{[2]},A_2^{[2]},
B_0^{[2]},B_1^{[2]},C_0^{[2]}$。
实际所有 85 个 kernel-current 列与它们的配对准确为零；已得 current 秩为 32，等于 $39-7$。所以
$
\boxed{\mathcal C(\ker Q)=\{v\in\mathbb Q^{39}:v\text{ 满足(4)}\}.}
\tag{5}
$
这是**本 144 标签模块**内的准确充要条件。所有公式为有理数，扩标量到实数时得到相应实像；(5)本身没有支付实际成本的正性、共同基准或具体根的有限评价秩。

例如 $A_1^{[0]}$ 可以和 $B_0^{[2]}$ 一起改变，满足第五关系；这说明某个单位向量不在像中，不能解释为对应系数完全不可改变。将十八个单位向量分别询问，恰有三个单独方向
$
A_0^{[0]},\quad A_0^{[1]},\quad A_0^{[2]}
$
是 MEMBER；其余十五个孤立单位目标不在这个 $\ker Q$ 的 current 像中。每条 nonmember 都保原完整 residual 和分离 annihilator，范围没有扩大到整个 $\mathcal R\cap\ker E$。

## 4. 原源重构、共同系数与输出完整性

此次新观察使用完整 Q 的一次消元，得到 85 个原 144 标签关系。对每个关系，用同一组系数重构全部三个原 Green current，共 255 个 moment-current 记录，再消元全部 39 坐标。

取得 32 个独立像代表及上述三个单独 A0 MEMBER 后，共 35 个不同原组合各自再次从**原 Q source 与三个完整原 current**重构，而不是只代回已消元矩阵。全部 35 个完整证书通过，包含 105 个重新构成的 moment-current；原 Q 及所有 current 重构差准确为零。这里是同一冻结原式实现的 fresh-source certificate，不冒充第二套独立实现。

同时完成的两个新接口检查是：

1. 带非零 c、真实二次尾及必须保留非局部原项的 Green/左锚接口；
2. 同一系数向量的共同 Q 核、严格 current 像及原组合重构接口。

没有调用旧开发套件、旧原 forcing 编译、旧 pure/operator rank 或具体 profile/Af 点评价。原源组装和此次新联合问题内的重构成本全部记入本次。

原日志中恰有 1020 个顺序数学记录，包括 18 个原算子、144 个完整 Q 列、144 步 Q 消元、85 个核核对、255 个原 moment-current、85 个完整 current 列、85 步像消元、7 条 annihilator、18 个目标，以及上述 fresh certificates 和两个新检查。最终摘要没有复制这批 payload。

root 读取原工作流输出后，只解析已经产生的记录并核对元数据：序号连续、每条 payload 字节与 SHA 一致、顺序 JSONL 指纹一致、身份链一致，十项源绑定逐路径/字节/哈希与冻结 request 完全相同。该读取没有新增符号消元或科学评价。

## 5. 实际来源与费用

唯一实际：
[run 43796872698](https://github.com/Rogerhu12/math-research-public/actions/runs/43796872698)，
[job 133067569306](https://github.com/Rogerhu12/math-research-public/actions/runs/43796872698/job/133067569306)，
source commit $\texttt{563defb46bc785295265c3f48fcad3fc8897c617}$，结论 success。job 于 2026-11-16 03:13:37—03:13:57 UTC 运行。

| 原输出/来源 | 字节数 | SHA256 |
|---|---:|---|
| 原 job log | 1322512 | 1edd4dd8ac34e2a9fe6fc1cf7ae08dc2d91fa279c02e6c32365bff9830e013b1 |
| COMPLETE JSON 加 LF | 15639 | c4b4031bddacca0c84050c7efdf8b43f80e7553553305d55dd52637f96af292d |
| 顺序 records JSONL，仅 runner 临时/原 stdout | 1170464 | dd936dc713d3461cfbf2652c4e88c89ac4b918eb7949bb379f3b940d62cb8ec7 |
| 冻结 request | 9269 | fd6e8526d6f7e9492911848b17a852d64a31654513a267ba61e5bdb9390ffb01 |
| 新 driver | 54281 | 18d5578869860f9da52d31137352f6a503a27610eab5e133b9a1c0f9ca85e8f5 |

1020 条身份链 SHA 为
$\texttt{673061557c1b53e78bf300d18e11e510d091378ad3431e159f6049404cde5101}$。
全部计算 payload 只保在原 Actions stdout 或 runner 临时文件；没有写入 Git、artifact、Release 或缓存。

| 真实收费项 | 实测 |
|---|---:|
| 新 science 时间 | 2.136164828999995 秒 |
| 两个新开发接口检查 | 0.002145778999988579 秒 |
| entry 总时间 | 2.184370506999997 秒 |
| science 峰值 RSS | 34076 KiB |
| development 峰值 RSS | 28176 KiB |
| science profile atoms | 495 |
| 受监测 rational 操作 / 最大 bits | 183164 / 48 |
| 新 mapper primitive / cache | 712 / 2318 |
| fresh mapper primitive / cache | 498 / 1711 |
| 合并 primitive / cache | 1210 / 4029 |

rational 操作仅按原监测边界收费，不声称已计所有继承表达式的底层算术。两个 mapper 的 cycle fallback 均为零，合并预算 overshoot 为零；没有因失败删掉已付阶段。原 180 秒、1 GiB 轮询 RSS、500000 次 primitive 与 300000 cache 的共同合同保留，未作续费重跑。

该 run 在研究前实际 pull：公开 03:13:48.835847—03:13:49.207936 UTC，前后均为上述 source；两 README 原 blob、空 diff、返回码零。私有 03:13:51.495633—03:13:52.386864，前后均为 $\texttt{b762edcd826d9f57138c530d0e5c854c37e119fe}$，根 README 无变化、题 README 不存在、QUEUE 中本会话唯一进行中。root 已读这些原收据，HANDOFF 同步登记。

## 6. 接入同一真实对象的剩余任务

(5)现在替代“还剩最多十八 formal 坐标”的未知接口：这个原模块的实际代数像已完整确定，可直接使用七条关系判断一个**共同三尾矩多项式目标**是否属于它，无须重跑这个研究目标。

但每个实际内部点的转换仍为
$
C_i=a_i^3\mathcal K_{n_i}(x_i),
$
其中 $x_i,u_i,p_i,r_i$、真实宽度、幅度及 suffix $n_i$ 都由同一个最终圆确定。不能给不同点分别选择(5)中的系数，不能将三个尾矩各求一个独立原成本再拼合，不能把 formal 32 视为某组实际根的 rank 32。

进一步与 R435/R436 的 self partial 组合时，还须同时保原 J⁺、原型与两次商修正的真实基准、whole C 的准确共同像、两个完整 period 目标和同一个二阶规范。最高层或某个局部 representative 的消去不能替代这些原值。整个响应空间可能还有本模块外的方向；七条关系没有被宣称为全空间障碍。

本结果完成的是一次新 joint 代数观察。全根 simultaneous flux、完整 period/同规范门、第四以上收敛、同一固定 g 的有限弯曲族及全部主课题几何门仍在进行。
