package sort

import "testing"

func TestSort_Standard(t *testing.T) {
	if got := Sort(10, 10, 10, 1); got != "STANDARD" {
		t.Fatalf("expected STANDARD, got %q", got)
	}
}

func TestSort_BulkyByVolumeThreshold(t *testing.T) {
	if got := Sort(100, 100, 100, 19); got != "SPECIAL" {
		t.Fatalf("expected SPECIAL, got %q", got)
	}
}

func TestSort_BulkyByDimensionThreshold(t *testing.T) {
	cases := []struct {
		w, h, l int
	}{
		{150, 10, 10},
		{10, 150, 10},
		{10, 10, 150},
	}

	for _, tc := range cases {
		if got := Sort(tc.w, tc.h, tc.l, 0); got != "SPECIAL" {
			t.Fatalf("expected SPECIAL for dims %v, got %q", tc, got)
		}
	}
}

func TestSort_HeavyByMassThreshold(t *testing.T) {
	if got := Sort(10, 10, 10, 20); got != "SPECIAL" {
		t.Fatalf("expected SPECIAL, got %q", got)
	}
}

func TestSort_RejectedWhenBoth(t *testing.T) {
	if got := Sort(150, 10, 10, 20); got != "REJECTED" {
		t.Fatalf("expected REJECTED, got %q", got)
	}
	if got := Sort(100, 100, 100, 20); got != "REJECTED" {
		t.Fatalf("expected REJECTED, got %q", got)
	}
}

func TestSort_PanicsOnNegativeInput(t *testing.T) {
	defer func() {
		if r := recover(); r == nil {
			t.Fatalf("expected panic on negative input")
		}
	}()
	_ = Sort(-1, 1, 1, 1)
}

