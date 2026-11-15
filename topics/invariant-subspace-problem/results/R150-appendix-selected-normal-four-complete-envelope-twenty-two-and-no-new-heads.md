# R150：normal≤4第二左包络恰22头与完整残差直和

日期：2026-11-15 UTC。Astra-ISP-789f；AI辅助，GPT-6 Astra Pro。

实际完成全部130个新增辅助单位右端、全部166列原残差和最终原第二方程。normal4校正没有增加旧22个头：完整联合残差秩为144，新130维残差空间与旧14维空间交为零。这个结论关闭normal≤4的支撑扩展；完整第二连接仍为 $9\le\beta_2\le11$，剩余normal5尚未处理。

## 1. 同一完整原族与本次精确判定

沿[完整normal4高核](R150-appendix-selected-normal-four-high-kernel130-and-residual-intersection.md)固定原 $I,J$ 和自然参数 $u$。完整高核为
$$
Z_4\in\mathbb Z^{1485\times130},\qquad
H_4Z_4=0,\qquad \operatorname{rank}_{\mathbb Q}H_4=1355.
$$
保旧原二阶族
$$
\begin{aligned}
\lambda_0&=\Lambda Cc,\\
\lambda_1&=E_{\rm old}Xc+\Lambda Ft+\Lambda Cy,\\
\lambda_2&=E_{\rm new}x+E_4Z_4\alpha+E_{\rm old}Xy+\Lambda e.
\end{aligned}
\tag{1.1}
$$
这里 $c,y\in\mathbb Q^{33}$、$t\in\mathbb Q^3$、$e\in\mathbb Q^{36}$，两个 $E$ 不交换，旧一阶纠偏 $X$ 不改支撑。实际方程为全部4354行
$$
M'_0x+M_4Z_4\alpha+[H_F,T](t,c)=0.
\tag{1.2}
$$

原 $M'_0$ 的同一1546阶单位块已用于旧36个右端。本次只对
$W=M_4Z_4$ 的130列求新单位解，每列保存正分母及全部1546个分子：
$$
(M'_0)_P N_j+D_jW_{P,j}=0.
\tag{1.3}
$$
五批为32、32、32、32、2；全部 $1546\cdot130=200980$ 个未除行content的原单位产品均实际核验。

逐列形成完整新残差
$$
S_{{\rm new},j}=M'_0N_j+D_jW_j\in\mathbb Z^{4354},
$$
复用旧36个已核原残差，构成
$$
S=[S_{\rm old},S_{\rm new}]\in\mathbb Z^{4354\times166}.
$$
每个新残差保全部4354原坐标，实际精确RREF给
$$
\boxed{\operatorname{rank}_{\mathbb Q}S=144.}
\tag{1.4}
$$

前稿已独立证明 $\operatorname{rank}S_{\rm old}=14$、
$\operatorname{rank}S_{\rm new}=130$。所以
$$
\boxed{\operatorname{im}S_{\rm old}\cap\operatorname{im}S_{\rm new}=0.}
\tag{1.5}
$$
特别，(1.2) 的任一解都迫 $\alpha=0$：其新残差必须落在上述交空间，随后新残差列独立给 $\alpha=0$。由 $M'_0$ 单射，旧支撑校正亦按原族恢复。normal4不是只在本次选出的22列上恰好为零；整个合法二阶族的normal4分量都被完整原方程迫零。

## 2. 22个真头与支撑完成范围

联合核维数为 $166-144=22$。按每列原分母恢复 $(t,c),x,\eta_4$，实际核得33行 $c$ 投影的有理秩为22；每个候选的全部4354原第二产品严格为零，共
$$
4354\cdot22=95788
$$
个坐标。完整 $y_{33}$、$e_{36}$ 自由保留，没有把零头方向计入。

旧真补空间 $E_{\rm new}$ 与完整常左核覆盖normal≤3的所有最后系数；$E_4$ 又包含同一 $I$ 的全部1485个normal4坐标。因此本次确实闭合原最后校正normal≤4的完整包络：
$$
\boxed{\dim\{\text{可用normal≤4最后校正的二阶leading头}\}=22.}
\tag{2.1}
$$
它与旧normal≤3 leading空间相同，而非另一个22维候选空间。

[第一连接恰3](R150-appendix-selected-natural-first-connection-exact-rank-three.md)及已付完整第二下界9仍给
$$
\boxed{9\le\beta_2\le11.}
\tag{2.2}
$$
normal5的1287个坐标还未排除；不能由 (2.1) 宣称完整第二连接等于11。指定无穷远阶91/88/88、K99与条件来源费8627保持，不因本条虚增。

## 3. 实际运行与全部来源

使用[完整130续接源码](../notes/2026-11-15-r150-selected-natural-second-left-normal-four-complete130-789f.py)及[精确接口](../notes/2026-11-15-r150-selected-natural-second-left-normal-four-complete130-interface-789f.md)。

- run43702348535；
- step selected-natural-second-left-normal-four-complete130；
- 执行源码提交df9062e41dee04d287e9e157b502a8a405d58fa5；
- 主源码SHA256为6b478e60d9508d977c156bf55bc0efc89205cf80b4a8ccf544547afebedb8ba6；
- 辅助worker SHA256为c9e1eee6142d29daf661682e177702825e90aef7222611baa2adadaffe0dc731；
- 数学预算600秒、每进程4096MiB；实际数学355.152873124秒、墙钟355.236334697秒，exit0、status completed；
- 实际outcome为restricted-second-left-support-only，准确表示 (2.1)，不是程序未完成。

完整绑定为672a21c0de59ec537f5d19333524f92ceb71ad3621eec643b9c11cf3f3fce2d3。

| 临时完整对象 | 字节数 | SHA256 |
|---|---:|---|
| 新130个单位解 | 75595833 | ccfdf7dbcc6b0d20ec5979a0c198df70f539f10669687ac9a0108f2706caae0d |
| 完整166列残差RREF | 25174 | 7e060678aa752228f8515e105726ad5335aaf403bb8965b19f6be796b25d1956 |
| 完整原产品回执 | 27679 | 4158cc3b978edeafd9c993e7f1c054d9acc419eb9a5d3f34cf8e9f2cff965c22 |

实际最终候选整数最大9628位。完整原小回执44867字节，SHA256为6383e6db6716a4fdab50e539a422ce814a407f9c794a75d61427385a9f98c461。[已推小记录](../notes/r150-infinity-remote-session-789f/43702348535-selected-natural-second-left-normal-four-complete130.json)保存各批实际完成状态、完整来源和全部输出哈希。

本次没有重算原高块、完整高核或旧36个单位解。新130解及全部原残差继续只在同一临时会话保存。下一步必须考虑normal5并保它对normal4高行的实际补偿；不能把 (1.5) 错用成允许normal5时normal4仍为零，也不能在尚无24头时启动以第二rank9为前提的第三页。
