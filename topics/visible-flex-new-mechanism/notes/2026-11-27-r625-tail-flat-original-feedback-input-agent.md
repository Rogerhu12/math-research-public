# R625 尾平输入进入原 R620 十九态全反馈

2026-11-27，会话 Astra-new-mechanism-1f4a61a4-20261127。
状态：输入纸证、纯源与明确范围；尚未有本 scope 的科学结果。

## 1. 这一次实际使用哪条输入

使用 [R625](../results/R625-true-terminal-acceleration-and-tail-flat-compatible-input.md)
的尾平曲线，R624 原未乘窗口的曲线只作已证比较对象，不执行其积分或选根。
中心仍为 R624 的负自由中心，十参数顺序保持
`H,v,p0c,p2c,s1c,r0c,a0,j0,f0,L`。
实际参数是

$$
(1,-1/2,-7/5,-1,-1/7,1/6,
a,j_b+400\pi^3q_\flat/9,-a\pi^2/9,3).
$$

这里 $a=1-T_1/(-S_1)$，$q_\flat$ 是

$$
\Phi_\flat(q)=B_c+C_2(q)\left(\frac{h_L^2}{1+(d_b+qD_\flat)^2}-1\right)=0
$$

在 $[0,1/15]$ 的唯一纸证根。
R624 给出的 $C_2(q)$ 与完整 $B''$ 交叉项保持不变；
只有真实末积分改为

$$
D_\flat=\frac{h_L}{2}\int_0^1
\frac{4\sin u\sin^2(20u)\cos^2u\,h_x}{h^2}\,dx,
\qquad u=\pi x/2.
$$

全程 h/k 为

$$
h=1+9a(1-\cos\pi x)/\pi^2,
$$
$$
k=-\frac85\sin u+\frac{8/5-3/\pi}{3}\sin3u
          +4q_\flat\sin u\sin^2(20u)\cos^2u.
$$

eta、八 A、六 rho 全部从这同一曲线和原中心真实积分。
两条完整首层末二阶方程未解，原八端也未强置零。
新输入的末几何 jets 通过 R625 必要符号 $T<-2/5$，
但这个模板条件不替真实历史、有限宽度 ruling 或任何主 README 门。

## 2. 新 helper 不执行旧输入

`scripts/r625_tail_flat_compatible_input_agent.py` 的
`TailFlatCompatibleFreeCenterInput` 继承 R624 的 constructor 成本壳和
`center_jets` 接口，完整覆盖 `_initialize` 与 `shape`。
父 constructor 调用的是新 `_initialize`，所以旧 R624 的 D、q 和曲线一次也不求值。
它只复用已发表的准确有理矩函数，所需矩最高次数10，
真实连续参考区间仍为 $[4.01,5.99]$。
这不是再生一份旧母诊断作为入口。
原十九行表与完整正 Gram 仍按主源同次必要重建一次并供整个 BVP 复用。

数值评价采用60位 mpmath、32固定分片 tanh-sinh、`maxdegree=7`，
基线 eta 用准确 atan 闭式，唯一新积分是上面的 $D_\flat$。
随后只做180次同一括号内的二分，没有扫描别的标量支。
所有实际次数、秒数、误差估计与原 bracket 符号均输出。
积分误差估计不是严格界；二分的评价 bracket 未包入积分误差，不能冒严格区间根。
因此输出参数是确切纸证输入的数值近似，准确首层常数等号只属于准确根。
任意选中的 $q\in[0,1/15]$ 都已有全段合法盒、动能余量和必要尾符号的纸面保证。

新 `shape` 中的窗口导数完整为

$$
w=\cos^2u,\quad w_u=-2\sin u\cos u,
\quad w_{uu}=2(\sin^2u-\cos^2u),
$$
$$
(\psi w)_u=\psi_uw+\psi w_u,
\quad(\psi w)_{uu}=\psi_{uu}w+2\psi_uw_u+\psi w_{uu}.
$$

中心物理 jets 来自同一曲线；末增量的前四个 Taylor 项为零。
最高半波频率43明确写入 receipt；没有把它冒称为41频。

## 3. 对尚未发布主源的准确改动范围

原未发布 `ExplicitFreeCenterInput` 类被删除，改为导入 R625 模型。
主程序创建一个独立 `input_progress` 字典并传给模型，
输入事件附完整模型 receipt，末事件报告该字典及实际 shape 点数。
模型初始化内任何异常或公开时钟 checkpoint 都经父 constructor 的
`finally` 记录部分积分/标量次数和时间。
原完整状态、最后接受态和已开始 fine 的保留规则不变。

其余全部19行、10个物理参数、左19真中心链、末8A+2速度、
完整 Jacobian、十末增量消元、原单位 Newton merit、全部历史与正势均不改。
存储 histories 仍要支付原微分方程和真实曲线积分差。
三常规范仍取 R620 的原有限宽度中心图，不能把这里的首层 C 常数直接替入。
原真实曲线门不放宽，LD 大势相消地板继续如实输出。

request 更新的只是这条实际输入身份、证明/helper绑定和新的明确费用项；
workflow 只补必要 sparse 路径和名称。
旧未发布明式中心输入和旧 R624 无窗口输入均不算实跑，累计费用账本不虚构零失败或成功。
R590 至 R616 的已有实际费用、自然终态与剩余缺口按原账本完整保留。

## 4. 原网格与真实精化的含义

首层继续32 Lobatto区间、65个观察节点；最高43半波对应每周期 $256/43$ 个观察间隔。
不能因此声称 quintic C² 重建就是解析 seed。
原 Gauss16 真历史读数仍实际观察这条初猜，而每次拟接受态读取的是其真正的 C² quintic曲线。
固定曲线 fine 保同物理参数和三常规范。
只有原配点19行与 stored10末门通过后，才进入已声明129观察点网格；
真实曲线全部门是独立的、更完整的原资格，不能被配点通过代替。

3300科学秒、180秒末预留、3120普通边界和90分钟 job上限保持。
新有理矩、端积分/二分、全部原表重建、试步、拒步、部分工作和真实再积分均计费。
所有科学执行只在公开 Actions，输出只在原 stdout，不保存 raw/表/trajectory/artifact/Release。
