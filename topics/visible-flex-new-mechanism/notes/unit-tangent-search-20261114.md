# 单位角切向表示的首次双圆领搜索

状态：**失败的有限搜索；无等距闭族**。独立脚本 `scripts/unit_tangent_collar_search.py` 使用
$$T=(-\sin\Theta\cos\Phi,\cos\Theta\cos\Phi,\sin\Phi),\qquad X=C(s)+a(s)\Pi T,$$
其中 $\Pi$ 为零均值角原函数，另显式求 $\int T\,d\theta=0$。当闭合准确时 $G=a^2$ 自动成立，余下求 $E=1,F=0$；保留三维中心 $C$，没有逐圈置中。角场和中心的五次B样条在两开圆领有零二jet。$a$ 在设计搜索中可变，不能称同一度量精化。

首轮 `controls=10,modes=4,offset=.02,angles=32,radial-order=6,max-nfev=80`，$2+3$曲率种子幅度`.25/.2`。解析Jacobian对一个固定方向中心差分的相对差为 $4.46\times10^{-10}$，是实现检查。实际LM停止后的细网格采样度量误差约`.00940335205`，角闭合均值约`.00203580801`，主曲率峰约`4.7941`，均不足以通过等距门槛。数据 `notes/unit-tangent-search-20261114/c10m4-e002.json`。

继续采用有符号Frenet角的完整向量残差，避免依赖正平方根或除以趋零的圆周法曲率。两个端口和完整度量仍要真正求解；本文件不声称路线成功或不可能。
