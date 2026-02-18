package sort

const (
	volumeBulkyThresholdCM3   int64 = 1000000
	dimensionBulkyThresholdCM int   = 150
	heavyThresholdKG          int   = 20
)

func Sort(width, height, length, mass int) string {
	if width < 0 || height < 0 || length < 0 || mass < 0 {
		panic("width, height, length, and mass must be >= 0")
	}

	volume := int64(width) * int64(height) * int64(length)
	bulky := volume >= volumeBulkyThresholdCM3 ||
		width >= dimensionBulkyThresholdCM ||
		height >= dimensionBulkyThresholdCM ||
		length >= dimensionBulkyThresholdCM
	heavy := mass >= heavyThresholdKG

	if bulky && heavy {
		return "REJECTED"
	}
	if bulky || heavy {
		return "SPECIAL"
	}
	return "STANDARD"
}

