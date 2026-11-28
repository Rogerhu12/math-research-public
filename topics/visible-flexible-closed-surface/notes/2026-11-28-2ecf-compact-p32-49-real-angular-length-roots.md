# 49 个真实非线性法向长度根与 48 次偶谐波新空间场

V44 的空间图和原冻结 192 度量不变地给出此步输入。另在同一基准法向上实加 $w(t)a(u)n$，其中 $w=64t^3(1-t)^3$。固定 $u$ 时，原实际新射线速度为 $V$，新速度是 $V+a(w'n+wn_t)$。在 $u_j=\pi j/96,0\le j\le48$ 各自解一元非线性长度方程
$
 \int_0^1|V+a(w'n+wn_t)|\,dt = \int_0^1\sqrt{Q(t)}\,dt .
$
每条射线合并实际 13、15 分母样条结点，在 27 个子段各用八点 Gauss。49 个求根系数从 −.002252286 至 .003697326，节点相对长度方程残差最多 $4.0\cdot10^{-15}$。这里的残差属真实 216 点积分计算；没有声明连续区间误差达到这个值。把 49 个根作 DCT-I，系数定义真实新场 $a(u)=\sum_{k=0}^{48}c_k\cos(2ku)$。在另一个 480 段的经向累计积分及 65 个角上，最大相对经长差约 $1.749\cdot10^{-6}$。之前同一 49 角的长度差有约 $-.0023533$ 至 $.0017928$。

新的整闭场仍是 R307 真闭面的法向图，物理位移至多 $1.06(.030573+.005842)<.03861<.097$，所以按 V44 的法向投影论证在所有相位嵌入。中央、两套端口与固定帽不变；径向各端的新增空间二 jets 为零。完整 G10 两组度量最大 .14269581，独立 G11 为 .14224801。G11 绝对主曲率峰 10.263501，支撑排球 .68030630，横向半宽 .88866752。原 14 物理行、材料长和实际两阶空间复合均保持。此步不具备原 R307 的独立 reach 证明。

从 topic 根目录、已有 V44 三个再生小输入运行

    node scripts/2ecf-compact-p32-angular-length-roots.mjs correct /tmp/p32-192.json /tmp/p32-clock.json /tmp/p32-normal84.json /tmp/p32-extra49.json
    node scripts/2ecf-compact-p32-angular-length-roots.mjs observeCorrection /tmp/p32-192.json /tmp/p32-clock.json /tmp/p32-normal84.json /tmp/p32-extra49.json

真实 49 系数规范 JSON 连末换行 SHA256 为 1fae3da4fcc580aee5758f8fa84e47c3d1ffac189918ac4060e302ff0bd395fe。
