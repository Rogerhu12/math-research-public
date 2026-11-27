# 原三来源辅助十三的完整 Hurwitz 校准

2026-11-27；会话 Astra-rank2-Sha-0b097461-20261127。

唯一公开计算 run **46029180230**，job **140608285958**，source **dd0da200f3abe8f1726f20e37e6ff367915e58c8**，15:55:46 UTC实际返回 PASS。入口 [check-original-three-source-quadratic-thirteen-hurwitz-rank.py](../scripts/check-original-three-source-quadratic-thirteen-hurwitz-rank.py) 只计算 $b=17$ 的三条原六 sigma 来源，保留 $-1/84$、原 $6\delta/39\delta$ 和所有六轴；没有目标 $p$ 扫描或中央值假定。

原三来源定义和全权差商已接回 [R1042](../results/R1042-original-three-canonical-common-norm81-carry-and-positive-grid.md) §14；本页登记已真实支付的有限输入。行序 $S,6\delta T,39\delta\Phi_{126}$，列序 $6,18,30$，$\delta^2=-3$。实际完整矩阵为
$$
\begin{pmatrix}
720&19475808299865538560&-217172351255436859174673625926074368000\\
4320\delta&-14627218514514143477760\delta&1765869213336073541779570472618664394752000\delta\\
28080\delta&-4821857646818361850920960\delta&-4004637195484950778226001018464590545027072000\delta
\end{pmatrix}.
$$
其有理整数行列式为
$$
-145944579624365231256538817659372783773537373634088867705498107904000000,
\qquad v_{13}=3,\qquad \Delta/13^3\equiv123\pmod{169}.
$$
各行的 $z^{12}/(b z^6)$ 比例分别为 $-988/105,-2938/35,15836/35$。整数 Hurwitz ODE 与独立 Laurent--指数递推逐系数核对到完整阶30一致；所有 $84H_{i,m}$ 在原 $\mathbf Z[\delta]$ 格中整。这里的有限矩阵是后继全差商证明所需的输入，不能凭三个点替代所有指标的证明，也不把目标 $p$ 赋值与辅助13赋值混同。

## 源与真实回执

- 源 SHA256：`81af6387e9f159c0780b8bc59e2cd3af4b3d80c271df2073b8dc156977d2efed`。
- 原 stdout：3099 bytes，SHA256 `0eef0a80052b082bfa16ff08fdbf6d26dbdad8be453d62bc52c8c0fd45dccbfb`。
- 已读完整 job log：11535 bytes，SHA256 `c3f8c2b27d4252deaf75f30c4e95cbce5ca917b2a064640617b5c571c566395f`。
- 原 sigma Hurwitz 全0至30摘要：`a48aa38ed4367cdb6e49c3167262ab708890d165cef5f04a7b743c6194cd36fc`。
- 校准 payload 摘要：`0ce7ffde61c5423c6dfba5e7efabb92d0c70cacec4f304654d7ba1faef944b26`。

未保存任何可重算输出或矩阵数据文件。以上九个必要系数和判别值是完整证明的有限输入。通常全 Sha 的无穷素数主目标尚未完成。
